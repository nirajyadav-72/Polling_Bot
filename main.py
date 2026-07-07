import os
import time
import sqlite3
import threading
from datetime import datetime
import pytz
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# दूसरी फाइल से प्रश्न इम्पोर्ट करें
from questions import QUIZ_LIST

# .env से सभी क्रेडेंشियल्स लोड करें
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

if not API_TOKEN:
    raise ValueError("Error: BOT_TOKEN एनवायरनमेंट वेरिएबल्स में नहीं मिला!")

bot = telebot.TeleBot(API_TOKEN)
DB_FILE = "bot_data.db"

if OWNER_ID:
    try:
        OWNER_ID = int(OWNER_ID)
    except ValueError:
        OWNER_ID = None

  # 💾 नया मार्किंग डेटाबेस आर्किटेक्चर (रीस्टार्ट प्रूफ)
def init_db():
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        # 1. ग्रुप्स सेटिंग्स टेबल
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                chat_id INTEGER PRIMARY KEY,
                current_index INTEGER DEFAULT 0,
                last_poll_id INTEGER DEFAULT NULL,
                last_sent_time REAL DEFAULT 0,
                language TEXT DEFAULT 'hindi',
                interval INTEGER DEFAULT 1800,
                auto_delete INTEGER DEFAULT 1
            )
        ''')
        # 2. यूज़र्स टेबल
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                user_name TEXT,
                join_time REAL
            )
        ''')
        # 3. पोल मैपिंग टेबल (सही उत्तर की आईडी के साथ)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS poll_mapping (
                poll_id TEXT PRIMARY KEY,
                chat_id INTEGER,
                correct_id INTEGER
            )
        ''')
        # 4. नया स्कोरिंग टेबल (+2 और -0.5 मार्किंग कैलकुलेशन के लिए)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_scores (
                chat_id INTEGER,
                user_id INTEGER,
                user_name TEXT,
                correct_count INTEGER DEFAULT 0,
                wrong_count INTEGER DEFAULT 0,
                PRIMARY KEY (chat_id, user_id)
            )
        ''')
        # 5. ओनर सेटिंग्स के लिए ग्लोबल टेबल
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bot_settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        cursor.execute("INSERT OR IGNORE INTO bot_settings (key, value) VALUES ('leaderboard_time', '22:00')")
        conn.commit()

init_db()

def is_user_admin(chat_id, user_id):
    if OWNER_ID and user_id == OWNER_ID:
        return True
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['creator', 'administrator']
    except Exception:
        return False

  # 🔄 ऑटोमैटिक पोल सेंडर लूप
def global_poll_manager():
    while True:
        try:
            with sqlite3.connect(DB_FILE, timeout=20) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT chat_id, current_index, last_poll_id, last_sent_time, language, interval, auto_delete FROM groups")
                all_groups = cursor.fetchall()
                current_now = time.time()

                for chat_id, current_index, last_poll_id, last_sent_time, language, interval, auto_delete in all_groups:
                    if current_now - last_sent_time >= interval:
                        
                        if last_poll_id is not None and auto_delete == 1:
                            try: bot.delete_message(chat_id=chat_id, message_id=last_poll_id)
                            except Exception: pass

                        filtered_quiz = [q for q in QUIZ_LIST if q.get("lang", "hindi") == language]
                        if not filtered_quiz:
                            filtered_quiz = QUIZ_LIST

                        if current_index >= len(filtered_quiz):
                            current_index = 0

                        quiz = filtered_quiz[current_index]
                        explanation_text = quiz.get("explanation", None)
                        
                        try:
                            sent_message = bot.send_poll(
                                chat_id=chat_id,
                                question=quiz["question"],
                                options=quiz["options"],
                                type="quiz",
                                correct_option_id=quiz["correct_id"],
                                is_anonymous=True,
                                explanation=explanation_text
                            )
                            new_poll_id = sent_message.message_id
                            poll_api_id = sent_message.poll.id
                            
                            cursor.execute("INSERT INTO poll_mapping (poll_id, chat_id, correct_id) VALUES (?, ?, ?)", 
                                           (poll_api_id, chat_id, quiz["correct_id"]))

                            new_index = (current_index + 1) % len(filtered_quiz)
                            cursor.execute('''
                                UPDATE groups 
                                SET current_index = ?, last_poll_id = ?, last_sent_time = ? 
                                WHERE chat_id = ?
                            ''', (new_index, new_poll_id, current_now, chat_id))
                            conn.commit()

                        except Exception as e:
                            if "bot was kicked" in str(e).lower() or "chat not found" in str(e).lower():
                                cursor.execute("DELETE FROM groups WHERE chat_id = ?", (chat_id,))
                                conn.commit()
        except Exception as db_err:
            print(f"डेटाबेस लूप एरर: {db_err}")
        time.sleep(5)

      # ⚙️ ग्रुप क्विज़ सेटिंग्स UI जेनरेटर
def get_settings_markup(chat_id):
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT language, interval, auto_delete FROM groups WHERE chat_id = ?", (chat_id,))
        res = cursor.fetchone()
    if not res: return None, None
    lang, interval, auto_delete = res[0], res[1], res[2]
    interval_mins = interval // 60
    del_status = "ON ✅" if auto_delete == 1 else "OFF 📴"
    
    text = (
        "⚙️ **ग्रुप क्विज़ सेटिंग्स (Quiz Settings)**\n\n"
        f"🌐 **वर्तमान भाषा (Language):** {lang.upper()}\n"
        f"⏱️ **क्विज़ अंतराल (Interval):** {interval_mins} मिनट\n"
        f"🗑️ **ऑटो-डिलीट स्टेटस:** {del_status}\n\n"
        "अपनी सेटिंग्स बदलने के लिए नीचे दिए गए बटनों का उपयोग करें:"
    )
    markup = InlineKeyboardMarkup()
    lang_text = "🌐 भाषा: HINDI 🇮🇳" if lang == 'hindi' else "🌐 Lang: ENGLISH 🇬🇧"
    btn_lang = InlineKeyboardButton(text=lang_text, callback_data=f"set_lang_{chat_id}")
    btn_autodel = InlineKeyboardButton(text="🗑️ Auto-Delete Settings", callback_data=f"menu_autodel_{chat_id}")
    btn_5m = InlineKeyboardButton(text="⏱️ 5 Min", callback_data=f"set_time_300_{chat_id}")
    btn_10m = InlineKeyboardButton(text="⏱️ 10 Min", callback_data=f"set_time_600_{chat_id}")
    btn_20m = InlineKeyboardButton(text="⏱️ 20 Min", callback_data=f"set_time_1200_{chat_id}")
    btn_30m = InlineKeyboardButton(text="⏱️ 30 Min", callback_data=f"set_time_1800_{chat_id}")
    btn_close = InlineKeyboardButton(text="Close ❌", callback_data=f"panel_close_{chat_id}")
    markup.row(btn_lang)
    markup.row(btn_autodel)
    markup.row(btn_5m, btn_10m)
    markup.row(btn_20m, btn_30m)
    markup.row(btn_close)
    return text, markup

# 🗑️ ऑटो-डिलीट सेटिंग्स सब-मेनू
def get_autodelete_markup(chat_id):
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT auto_delete FROM groups WHERE chat_id = ?", (chat_id,))
        res = cursor.fetchone()
    auto_delete = res[0] if res else 1
    status_text = "ON" if auto_delete == 1 else "OFF"
    text = (
        "🗑️ **Auto-Delete Settings**\n\n"
        f"📊 **Status:** \" {status_text} \"\n\n"
        "👇 Change auto-delete setting:"
    )
    markup = InlineKeyboardMarkup()
    btn_on = InlineKeyboardButton(text="Turn On ✅", callback_data=f"autodel_on_{chat_id}")
    btn_off = InlineKeyboardButton(text="Turn Off 📴", callback_data=f"autodel_off_{chat_id}")
    btn_back = InlineKeyboardButton(text="Back 🔙", callback_data=f"autodel_back_{chat_id}")
    markup.row(btn_on, btn_off)
    markup.row(btn_back)
    return text, markup

  @bot.message_handler(commands=['settings'], chat_types=['group', 'supergroup'])
def group_settings(message):
    if not is_user_admin(message.chat.id, message.from_user.id):
        try: bot.reply_to(message, "❌ केवल ग्रुप के एडमिन ही सेटिंग्स बदल सकते हैं।")
        except Exception: pass
        return
    text, markup = get_settings_markup(message.chat.id)
    if text:
        try: bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")
        except Exception: pass

@bot.callback_query_handler(func=lambda call: call.data.startswith(('set_lang_', 'set_time_', 'menu_autodel_', 'autodel_', 'panel_close_')))
def handle_settings_callbacks(call):
    user_id = call.from_user.id
    data_parts = call.data.split('_')
    action = data_parts[0]       
    sub_action = data_parts[1]   
    chat_id = int(data_parts[-1]) 
    
    if not is_user_admin(chat_id, user_id):
        bot.answer_callback_query(call.id, "❌ आपके पास एडमिन परमिशन नहीं है!", show_alert=True)
        return

    if action == "panel" and sub_action == "close":
        try:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.answer_callback_query(call.id, "सेटिंग्स पैनल बंद कर दिया गया।")
        except Exception: pass
        return

    show_main_menu = True
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        if action == "set" and sub_action == "lang":
            cursor.execute("SELECT language FROM groups WHERE chat_id = ?", (chat_id,))
            res = cursor.fetchone()
            current_lang = res[0] if res else 'hindi'
            new_lang = 'english' if current_lang == 'hindi' else 'hindi'
            cursor.execute("UPDATE groups SET language = ? WHERE chat_id = ?", (new_lang, chat_id))
            bot.answer_callback_query(call.id, f"भाषा बदलकर {new_lang.upper()} कर दी गई है।")
        elif action == "set" and sub_action == "time":
            new_interval = int(data_parts[2]) 
            cursor.execute("UPDATE groups SET interval = ? WHERE chat_id = ?", (new_interval, chat_id))
            bot.answer_callback_query(call.id, f"समय अंतराल बदलकर {new_interval // 60} मिनट कर दिया गया है।")
        elif action == "menu" and sub_action == "autodel":
            show_main_menu = False
            bot.answer_callback_query(call.id) 
        elif action == "autodel":
            if sub_action == "on":
                cursor.execute("UPDATE groups SET auto_delete = 1 WHERE chat_id = ?", (chat_id,))
                bot.answer_callback_query(call.id, "Auto-Delete चालू (ON) कर दिया गया है।")
                show_main_menu = False
            elif sub_action == "off":
                cursor.execute("UPDATE groups SET auto_delete = 0 WHERE chat_id = ?", (chat_id,))
                bot.answer_callback_query(call.id, "Auto-Delete बंद (OFF) कर दिया गया है।")
                show_main_menu = False
            elif sub_action == "back":
                bot.answer_callback_query(call.id, "मुख्य मेनू पर वापस जा रहे हैं...")
                show_main_menu = True
        conn.commit()
        
    if show_main_menu: text, markup = get_settings_markup(chat_id)
    else: text, markup = get_autodelete_markup(chat_id)
    try: bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode="Markdown")
    except Exception: pass

  # 👑 ओनर कमांड - ऑटो लीडरबोर्ड टाइम सेट करना
@bot.message_handler(commands=['settime'], chat_types=['private'])
def set_global_leaderboard_time(message):
    if not (OWNER_ID and message.from_user.id == OWNER_ID):
        bot.send_message(message.chat.id, "❌ यह कमांड सिर्फ बॉट ओनर के लिए है।")
        return
    args = message.text.split()
    if len(args) < 2:
        bot.send_message(message.chat.id, "⚠️ फॉर्मेट: `/settime 22:00`", parse_mode="Markdown")
        return
    time_str = args[1].strip()
    try:
        datetime.strptime(time_str, "%H:%M")
        with sqlite3.connect(DB_FILE, timeout=20) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE bot_settings SET value = ? WHERE key = 'leaderboard_time'", (time_str,))
            conn.commit()
        bot.send_message(message.chat.id, f"✅ दैनिक रिज़ल्ट अब **{time_str}** बजे ऑटो-सेंड होगा।")
    except ValueError:
        bot.send_message(message.chat.id, "❌ अमान्य फॉर्मेट (उदाहरण: 22:30)।")

# 📢 ओनर कमांड - ब्रॉडकास्ट फ़ीचर
@bot.message_handler(commands=['broadcast'], chat_types=['private'])
def handle_owner_broadcast(message):
    if not (OWNER_ID and message.from_user.id == OWNER_ID): return
    if not message.reply_to_message:
        bot.send_message(message.chat.id, "⚠️ मैसेज पर **Reply** करके लिखें: `/broadcast`")
        return
    target_msg = message.reply_to_message
    status_msg = bot.send_message(message.chat.id, "📢 ब्रॉडकास्ट शुरू...")
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT chat_id FROM groups"); all_chats = cursor.fetchall()
        cursor.execute("SELECT user_id FROM users"); all_users = cursor.fetchall()
    g_s, u_s = 0, 0
    for (chat_id,) in all_chats:
        try: bot.copy_message(chat_id=chat_id, from_chat_id=message.chat.id, message_id=target_msg.message_id); g_s+=1; time.sleep(0.05)
        except Exception: pass
    for (user_id,) in all_users:
        try: bot.copy_message(chat_id=user_id, from_chat_id=message.chat.id, message_id=target_msg.message_id); u_s+=1; time.sleep(0.05)
        except Exception: pass
    bot.edit_message_text(chat_id=message.chat.id, message_id=status_msg.message_id, text=f"📊 सफल ग्रुप्स: {g_s} | यूज़र्स: {u_s}")

# 👑 🏆 ओनर कमांड - मैनुअल लीडरबोर्ड सेंडर (न्यू मार्किंग के साथ)
@bot.message_handler(commands=['sendresult'], chat_types=['private'])
def manual_leaderboard_sender(message):
    if not (OWNER_ID and message.from_user.id == OWNER_ID): return
    status_msg = bot.send_message(message.chat.id, "⏳ **सभी ग्रुप्स में तुरंत नया रिज़ल्ट भेजा जा रहा है...**")
    IST = pytz.timezone('Asia/Kolkata')
    now = datetime.now(IST)
    
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT chat_id FROM groups")
        all_chats = cursor.fetchall()
        success_count = 0
        
        for (chat_id,) in all_chats:
            cursor.execute("SELECT user_name, correct_count, wrong_count FROM daily_scores WHERE chat_id = ?", (chat_id,))
            all_users = cursor.fetchall()
            
            calculated_leaderboard = []
            for name, correct, wrong in all_users:
                final_score = (correct * 2) - (wrong * 0.5)
                if (correct + wrong) > 0:
                    calculated_leaderboard.append((name, correct, wrong, final_score))
            
            calculated_leaderboard.sort(key=lambda x: x[3], reverse=True)
            top_20 = calculated_leaderboard[:20]
            
            lb_text = "🏆 **दैनिक क्विज़ रिज़ल्ट (Top 20 Leaderboard)** 🏆\n"
            lb_text += f"📅 दिनांक: {now.strftime('%d-%m-%Y')} | समय: {now.strftime('%H:%M')} (मैनुअल)\n"
            lb_text += "📊 मार्किंग: सही (+2) | गलत (-0.5)\n\n"
            
            if top_20:
                medals = {1: "🥇", 2: "🥈", 3: "🥉"}
                for idx, (name, correct, wrong, final_score) in enumerate(top_20, 1):
                    medal = medals.get(idx, f"{idx}.")
                    lb_text += f"{medal} **{name}** — {final_score} pts (✅{correct} | ❌{wrong})\n"
            else:
                lb_text += "⚠️ आज किसी भी यूजर ने क्विज़ में भाग नहीं लिया।"
                
            lb_text += "\n🎯 अद्भुत प्रयास! कल नए क्विज़ के लिए तैयार रहें।"
            try: bot.send_message(chat_id=chat_id, text=lb_text, parse_mode="Markdown"); success_count+=1; time.sleep(0.05)
            except Exception: pass
            
        cursor.execute("DELETE FROM daily_scores")
        cursor.execute("DELETE FROM poll_mapping")
        conn.commit()
    bot.edit_message_text(chat_id=message.chat.id, message_id=status_msg.message_id, text=f"✅ मैनुअल रिज़ल्ट कुल **{success_count}** ग्रुप्स में भेजा गया।")

  # 🏆 दैनिक लीडरबोर्ड (ऑटोमैटिक शेड्यूलर - न्यू मार्किंग)
def daily_leaderboard_scheduler():
    has_sent_today = False
    last_checked_date = ""
    while True:
        try:
            IST = pytz.timezone('Asia/Kolkata')
            now = datetime.now(IST)
            current_date_str = now.strftime("%Y-%m-%d")
            if current_date_str != last_checked_date:
                has_sent_today = False
                last_checked_date = current_date_str

            with sqlite3.connect(DB_FILE, timeout=20) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT value FROM bot_settings WHERE key = 'leaderboard_time'")
                res = cursor.fetchone()
                db_time = res[0] if res else "22:00"
            target_hour, target_minute = map(int, db_time.split(':'))
            
            if now.hour == target_hour and now.minute == target_minute and not has_sent_today:
                with sqlite3.connect(DB_FILE, timeout=20) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT chat_id FROM groups"); all_chats = cursor.fetchall()
                    for (chat_id,) in all_chats:
                        cursor.execute("SELECT user_name, correct_count, wrong_count FROM daily_scores WHERE chat_id = ?", (chat_id,))
                        all_users = cursor.fetchall()
                        calculated_leaderboard = []
                        for name, correct, wrong in all_users:
                            final_score = (correct * 2) - (wrong * 0.5)
                            if (correct + wrong) > 0:
                                calculated_leaderboard.append((name, correct, wrong, final_score))
                        calculated_leaderboard.sort(key=lambda x: x[3], reverse=True)
                        top_20 = calculated_leaderboard[:20]
                        lb_text = "🏆 **दैनिक क्विज़ रिज़ल्ट (Top 20 Leaderboard)** 🏆\n"
                        lb_text += f"📅 दिनांक: {now.strftime('%d-%m-%Y')} | समय: {db_time}\n"
                        lb_text += "📊 मार्किंग: सही (+2) | गलत (-0.5)\n\n"
                        if top_20:
                            medals = {1: "🥇", 2: "🥈", 3: "🥉"}
                            for idx, (name, correct, wrong, final_score) in enumerate(top_20, 1):
                                medal = medals.get(idx, f"{idx}.")
                                lb_text += f"{medal} **{name}** — {final_score} pts (✅{correct} | ❌{wrong})\n"
                        else: lb_text += "⚠️ पिछले 24 घंटों में किसी ने भाग नहीं लिया।"
                        try: bot.send_message(chat_id=chat_id, text=lb_text, parse_mode="Markdown"); time.sleep(0.05)
                        except Exception: pass
                    cursor.execute("DELETE FROM daily_scores")
                    cursor.execute("DELETE FROM poll_mapping")
                    conn.commit()
                has_sent_today = True
                time.sleep(60) 
        except Exception as e: print(f"शेड्यूलर एरर: {e}")
        time.sleep(20)

# 🎯 LIVE पोल उत्तर ट्रैकर (न्यू मार्किंग 100% फिक्स लॉजिक)
@bot.poll_answer_handler()
def handle_poll_answer(poll_answer):
    poll_id = poll_answer.poll_id
    user_id = poll_answer.user.id
    first_name = poll_answer.user.first_name if poll_answer.user.first_name else ""
    last_name = poll_answer.user.last_name if poll_answer.user.last_name else ""
    user_name = f"{first_name} {last_name}".strip()
    if not user_name: user_name = f"User_{user_id}"

    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT chat_id, correct_id FROM poll_mapping WHERE poll_id = ?", (poll_id,))
        mapping = cursor.fetchone()
        
        if mapping and poll_answer.option_ids:
            chat_id = mapping[0]
            correct_id = mapping[1]
            chosen_option = poll_answer.option_ids[0]
            
            if chosen_option == correct_id:
                cursor.execute('''
                    INSERT INTO daily_scores (chat_id, user_id, user_name, correct_count, wrong_count)
                    VALUES (?, ?, ?, 1, 0) ON CONFLICT(chat_id, user_id) DO UPDATE SET
                    user_name = excluded.user_name, correct_count = correct_count + 1
                ''', (chat_id, user_id, user_name))
            else:
                cursor.execute('''
                    INSERT INTO daily_scores (chat_id, user_id, user_name, correct_count, wrong_count)
                    VALUES (?, ?, ?, 0, 1) ON CONFLICT(chat_id, user_id) DO UPDATE SET
                    user_name = excluded.user_name, wrong_count = wrong_count + 1
                ''', (chat_id, user_id, user_name))
            conn.commit()

          # 📊 यूजर लाइव स्कोर ट्रैकर कमांड
@bot.message_handler(commands=['myscore'])
def check_user_score(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT correct_count, wrong_count FROM daily_scores WHERE chat_id = ? AND user_id = ?", (chat_id, user_id))
        res = cursor.fetchone()
    if res:
        correct, wrong = res[0], res[1]
        final_score = (correct * 2) - (wrong * 0.5)
    else: correct, wrong, final_score = 0, 0, 0.0
    try:
        score_text = f"🎯 **{message.from_user.first_name}**, आपका लाइव स्कोर:\n\n✅ सही: **{correct}** (+{correct*2})\n❌ गलत: **{wrong}** (-{wrong*0.5})\n🔥 **फाइनल स्कोर: {final_score}导 पॉइंट्स**"
        bot.reply_to(message, score_text, parse_mode="Markdown")
    except Exception: pass

# 💬 /start कमांड
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if message.chat.type in ['group', 'supergroup']:
        try: bot.reply_to(message, text=f"👋 नमस्ते!\n🤖 मैं इस ग्रुप में एक्टिव हूँ। एडमिन ध्यान दें: कस्टमाइज करने के लिए ग्रुप में `/settings` टाइप करें।")
        except Exception: pass
        return
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (user_id, user_name, join_time) VALUES (?, ?, ?)", (user_id, message.from_user.first_name, time.time()))
        cursor.execute("SELECT value FROM bot_settings WHERE key = 'leaderboard_time'")
        res = cursor.fetchone(); db_time = res[0] if res else "22:00"
        conn.commit()
    if OWNER_ID and user_id == OWNER_ID:
        w_text = f"👑 **प्रणाम मालिक!**\n\n📊 लीडरबोर्ड टाइम: **{db_time}**\n🏆 तुरंत रिज़ल्ट भेजने के लिए: `/sendresult`"
    else: w_text = "👋 नमस्ते! मैं एडवांस क्विज़ शेड्यूलर बॉट हूँ।"
    markup = InlineKeyboardMarkup()
    try: url = f"https://t.me/{bot.get_me().username}?startgroup=true"
    except Exception: url = "https://t.me/BotFather"
    markup.add(InlineKeyboardButton(text="➕ Add Me To Your Group ➕", url=url))
    try: bot.send_message(chat_id=message.chat.id, text=w_text, reply_markup=markup, parse_mode="Markdown")
    except Exception: pass

# ℹ️ हेल्प कमांड
@bot.message_handler(commands=['help'])
def send_help(message):
    try: bot.send_message(chat_id=message.chat.id, text="❓ ग्रुप के अंदर `/settings` कमांड चलाकर कस्टमाइज़ करें। बॉट एडमिन होना चाहिए।")
    except Exception: pass

# 📊 लाइव स्टेटस
@bot.message_handler(commands=['status'])
def send_stats(message):
    if not (OWNER_ID and message.from_user.id == OWNER_ID): return
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM groups"); g_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM users"); u_count = cursor.fetchone()[0]
    bot.send_message(message.chat.id, f"📊 **बॉट लाइव स्टेटस:**\n\n🎯 ग्रुप्स: **{g_count}**\n👤 यूज़र्स: **{u_count}**")

@bot.my_chat_member_handler()
def handle_left_or_joined(message):
    new_status = message.new_chat_member.status
    with sqlite3.connect(DB_FILE, timeout=20) as conn:
        cursor = conn.cursor()
        if new_status in ["administrator", "member"]:
            cursor.execute("INSERT OR IGNORE INTO groups (chat_id, interval) VALUES (?, 1800)", (message.chat.id,))
            cursor.execute("UPDATE groups SET last_sent_time = 0 WHERE chat_id = ?", (message.chat.id,))
            conn.commit()
            try: bot.send_message(chat_id=message.chat.id, text="🎉 **बॉट सफलतापूर्वक एक्टिव हो चुका है!**")
            except Exception: pass
        elif new_status in ["left", "kicked"]:
            cursor.execute("DELETE FROM groups WHERE chat_id = ?", (message.chat.id,))
            conn.commit()

# बैकग्राउंड थ्रेड्स शुरू करें
threading.Thread(target=global_poll_manager, daemon=True).start()
threading.Thread(target=daily_leaderboard_scheduler, daemon=True).start()

print("successfully deploy...🚀")
bot.infinity_polling(allowed_updates=["my_chat_member", "message", "callback_query", "poll_answer"], timeout=60, skip_pending=True)
          
