# 📚 टेलीग्राम क्विज़ बॉट प्रश्न बैंक (Question Bank) - भाग 1

QUIZ_LIST = [
    # =========================================================
    # ------------------- Samvidhan QUIZZES -------------------
    # =========================================================
    {
        "question": "भारत का सबसे ऊँचा जलप्रपात (Waterfall) कुंचिकल कहाँ स्थित है?\n\n[SSC GD 10-Jan-2023 Shift-3]",
        "options": ["केरल", "कर्नाटक", "तमिलनाडु", "ओडिशा"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 वराही नदी पर बना कुंचिकल जलप्रपात कर्नाटक में स्थित है, जो भारत का सबसे ऊँचा जलप्रपात है।"
    },
    {
        "question": "सौरमंडल के किस ग्रह के पास सबसे अधिक उपग्रह (Moons) हैं?\n\n[SSC MTS 04-May-2023 Shift-2]",
        "options": ["मंगल", "बृहस्पति", "शनि", "वरुण"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 सौरमंडल में शनि (Saturn) ग्रह के पास वर्तमान में सबसे अधिक चंद्रमा (उपग्रह) हैं।"
    },
    {
        "question": "भारत में 'काली क्रांति' (Black Revolution) किससे संबंधित है?\n\n[SSC CHSL 16-Mar-2023 Shift-1]",
        "options": ["कोयला उत्पादन", "कच्चा तेल (पेट्रोलियम)", "काली मिर्च", "सरसों उत्पादन"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 काली क्रांति का संबंध पेट्रोलियम या कच्चे तेल (Crude Oil) के उत्पादन को बढ़ाने से है।"
    },
    {
        "question": "नाथू ला दर्रा (Nathu La Pass) भारत के किस राज्य में स्थित है?\n\n[SSC GD 13-Jan-2023 Shift-1]",
        "options": ["उत्तराखंड", "हिमाचल प्रदेश", "सिक्किम", "अरुणाचल प्रदेश"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 नाथू ला दर्रा सिक्किम राज्य में स्थित है, जो भारत और चीन (तिब्बत) को जोड़ता है।"
    },
    {
        "question": "काजीरंगा राष्ट्रीय उद्यान (Kaziranga National Park) किसके लिए प्रसिद्ध है?\n\n[SSC MTS 12-May-2023 Shift-3]",
        "options": ["एक सींग वाला गैंडा", "रॉयल बंगाल टाइगर", "एशियाई शेर", "घड़ियाल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 असम में स्थित काजीरंगा राष्ट्रीय उद्यान एक सींग वाले गैंडे (One-horned Rhinoceros) के लिए विश्व प्रसिद्ध है।"
    },
    {
        "question": "भारत की सबसे बड़ी खारे पानी की झील (Saltwater Lake) कौन सी है?\n\n[SSC CHSL 14-Mar-2023 Shift-3]",
        "options": ["सांभर झील", "चिल्का झील", "लोनार झील", "पुलिकट झील"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 ओडिशा में स्थित चिल्का झील भारत की सबसे बड़ी खारे पानी की लैगून झील है।"
    },
    {
        "question": "दक्षिण भारत की सबसे ऊँची चोटी कौन सी है?\n\n[SSC GD 27-Jan-2023 Shift-1]",
        "options": ["डोडाबेटा", "अनामुडी", "महेंद्रगिरि", "कलसुबाई"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 अनामुडी (Anamudi) दक्षिण भारत और पश्चिमी घाट की सबसे ऊँची चोटी है, जिसकी ऊँचाई 2695 मीटर है।"
    },
    {
        "question": "खेतड़ी (Khetri) की खानें किसके उत्पादन के लिए प्रसिद्ध हैं?\n\n[SSC MTS 16-Jun-2023 Shift-2]",
        "options": ["लोहा", "कोयला", "तांबा", "सोना"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 राजस्थान के झुंझुनू जिले में स्थित खेतड़ी की खानें तांबे (Copper) के खनन के लिए प्रसिद्ध हैं।"
    },
    {
        "question": "कावेरी नदी जल विवाद मुख्य रूप से किन दो राज्यों के बीच है?\n\n[SSC GD 06-Feb-2023 Shift-4]",
        "options": ["केरल और कर्नाटक", "कर्नाटक और तमिलनाडु", "तमिलनाडु और आंध्र प्रदेश", "केरल और आंध्र प्रदेश"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 कावेरी नदी के पानी के बँटवारे को लेकर मुख्य विवाद कर्नाटक और तमिलनाडु राज्यों के बीच है।"
    },
    {
        "question": "Where is Kunchikal, the highest waterfall in India, located?\n\n[SSC GD 10-Jan-2023 Shift-3]",
        "options": ["Kerala", "Karnataka", "Tamil Nadu", "Odisha"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Kunchikal Falls, formed by the Varahi river, is located in Karnataka and is the highest waterfall in India."
    },
    {
        "question": "Which planet in our solar system has the maximum number of moons?\n\n[SSC MTS 04-May-2023 Shift-2]",
        "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Saturn currently holds the record for the maximum number of natural satellites (moons) in the solar system."
    },
    {
        "question": "With what is the 'Black Revolution' in India associated?\n\n[SSC CHSL 16-Mar-2023 Shift-1]",
        "options": ["Coal production", "Crude Oil (Petroleum)", "Black Pepper", "Mustard production"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Black Revolution is related to increasing the production of petroleum or crude oil."
    },
    {
        "question": "In which Indian state is the Nathu La Pass located?\n\n[SSC GD 13-Jan-2023 Shift-1]",
        "options": ["Uttarakhand", "Himachal Pradesh", "Sikkim", "Arunachal Pradesh"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Nathu La Pass is located in the state of Sikkim, connecting India with Tibet (China)."
    },
    {
        "question": "For what is the Kaziranga National Park famous?\n\n[SSC MTS 12-May-2023 Shift-3]",
        "options": ["One-horned Rhinoceros", "Royal Bengal Tiger", "Asiatic Lion", "Gharial"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Kaziranga National Park, located in Assam, is world-famous for the endangered one-horned rhinoceros."
    },
    {
        "question": "Which is the largest saltwater lake in India?\n\n[SSC CHSL 14-Mar-2023 Shift-3]",
        "options": ["Sambhar Lake", "Chilika Lake", "Lonar Lake", "Pulicat Lake"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Chilika Lake, located in Odisha, is the largest brackish saltwater lagoon lake in India."
    },
    {
        "question": "Which is the highest peak in South India?\n\n[SSC GD 27-Jan-2023 Shift-1]",
        "options": ["Doddabetta", "Anamudi", "Mahendragiri", "Kalsubai"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Anamudi is the highest peak in South India and the Western Ghats, with an elevation of 2695 meters."
    },
    {
        "question": "The mines of Khetri are famous for the production of which mineral?\n\n[SSC MTS 16-Jun-2023 Shift-2]",
        "options": ["Iron", "Coal", "Copper", "Gold"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Khetri mines, located in the Jhunjhunu district of Rajasthan, are famous for copper mining."
    },
    {
        "question": "The Cauvery river water dispute is primarily between which two states?\n\n[SSC GD 06-Feb-2023 Shift-4]",
        "options": ["Kerala and Karnataka", "Karnataka and Tamil Nadu", "Tamil Nadu and Andhra Pradesh", "Kerala and Andhra Pradesh"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The core dispute over the sharing of Cauvery river water is between the states of Karnataka and Tamil Nadu."
    },
    {
        "question": "Through how many Indian states does the Tropic of Cancer pass?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["6 states", "7 states", "8 states", "9 states"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Tropic of Cancer passes through 8 Indian states (Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram)."
    },
    {
        "question": "कर्क रेखा (Tropic of Cancer) भारत के कितने राज्यों से होकर गुजरती है?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["6 राज्यों", "7 राज्यों", "8 राज्यों", "9 राज्यों"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 कर्क रेखा भारत के बीचों-बीच से कुल 8 राज्यों (गुजरात, राजस्थान, मप्र, छत्तीसगढ़, झारखंड, प. बंगाल, त्रिपुरा, मिजोरम) से गुजरती है।"
    },
    {
        "question": "भारत का सबसे लंबा राष्ट्रीय राजमार्ग (National Highway) कौन सा है?\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["NH 1", "NH 7", "NH 10", "NH 44"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 राष्ट्रीय राजमार्ग 44 (NH 44) भारत का सबसे लंबा राजमार्ग है, जो श्रीनगर से कन्याकुमारी तक जाता है।"
    },
    {
        "question": "किस ग्रह को पृथ्वी की 'जुड़वां बहन' (Earth's Twin) कहा जाता है?\n\n[SSC MTS 03-May-2023 Shift-1]",
        "options": ["बुध", "शुक्र", "मंगल", "शनि"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 आकार, द्रव्यमान और घनत्व में पृथ्वी के समान होने के कारण शुक्र (Venus) को पृथ्वी की जुड़वां बहन कहा जाता है।"
    },
    {
        "question": "भारत में सबसे बड़ा काजू उत्पादक राज्य कौन सा है?\n\n[SSC CHSL 15-Mar-2023 Shift-3]",
        "options": ["केरल", "महाराष्ट्र", "आंध्र प्रदेश", "तमिलनाडु"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 महाराष्ट्र भारत का सबसे प्रमुख और बड़ा काजू उत्पादक राज्य है।"
    },
    {
        "question": "सुंदरवन राष्ट्रीय उद्यान (Sundarbans National Park) भारत के किस राज्य में स्थित है?\n\n[SSC GD 17-Jan-2023 Shift-4]",
        "options": ["ओडिशा", "असम", "पश्चिम बंगाल", "बिहार"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 सुंदरवन राष्ट्रीय उद्यान पश्चिम बंगाल में स्थित है, जो रॉयल बंगाल टाइगर और मैंग्रोव वनों के लिए प्रसिद्ध है।"
    },
    {
        "question": "भारत और श्रीलंका को अलग करने वाली जलसंधि (Strait) को क्या कहते हैं?\n\n[SSC MTS 10-May-2023 Shift-3]",
        "options": ["पाक जलडमरूमध्य", "मलक्का जलसंधि", "बेरिंग जलसंधि", "10 डिग्री चैनल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 पाक जलडमरूमध्य (Palk Strait) भारत (तमिलनाडु) और श्रीलंका के मन्नार जिले को अलग करता है।"
    },
    {
        "question": "भारत में 'गुलाबी क्रांति' (Pink Revolution) किससे संबंधित है?\n\n[SSC CHSL 14-Mar-2023 Shift-1]",
        "options": ["टमाटर उत्पादन", "झींगा और प्याज उत्पादन", "मांस उत्पादन", "उर्वरक उत्पादन"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 गुलाबी क्रांति का संबंध झींगा मछली (Prawn) और प्याज (Onion) के उत्पादन से है।"
    },
    {
        "question": "हीराकुड बांध (Hirakud Dam) किस नदी पर निर्मित है?\n\n[SSC GD 25-Jan-2023 Shift-2]",
        "options": ["गंगा", "गोदावरी", "महानदी", "कृष्णा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 ओडिशा में महानदी पर बना हीराकुड बांध भारत का सबसे लंबा बांध है।"
    },
    {
        "question": "हीरे की खदानों के लिए प्रसिद्ध 'पन्ना' (Panna) किस राज्य में स्थित है?\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["राजस्थान", "मध्य प्रदेश", "झारखंड", "छत्तीसगढ़"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 मध्य प्रदेश का पन्ना जिला भारत में हीरे की प्रमुख खदानों के लिए विश्व प्रसिद्ध है।"
    },
    {
        "question": "भारत की सबसे बड़ी मीठे पानी की झील (Freshwater Lake) कौन सी है?\n\n[SSC GD 03-Feb-2023 Shift-3]",
        "options": ["चिल्का झील", "वुलर झील", "सांभर झील", "दल झील"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 जम्मू-कश्मीर में स्थित वुलर झील भारत की सबसे बड़ी मीठे पानी की झील है।"
    },
    {
        "question": "निम्नलिखित में से किस राज्य की तटरेखा (Coastline) सबसे लंबी है?\n\n[SSC CHSL 17-Mar-2023 Shift-4]",
        "options": ["महाराष्ट्र", "तमिलनाडु", "गुजरात", "आंध्र प्रदेश"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भारत में गुजरात राज्य की समुद्र तटरेखा सबसे लंबी (लगभग 1600 किमी) है।"
    },
    {
        "question": "Which is the longest National Highway in India?\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["NH 1", "NH 7", "NH 10", "NH 44"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 National Highway 44 (NH 44) is the longest highway in India, running from Srinagar to Kanyakumari."
    },
    {
        "question": "Which planet is known as 'Earth's Twin'?\n\n[SSC MTS 03-May-2023 Shift-1]",
        "options": ["Mercury", "Venus", "Mars", "Saturn"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Venus is called Earth's twin due to its similar size, mass, and density to Earth."
    },
    {
        "question": "Which is the largest cashew-producing state in India?\n\n[SSC CHSL 15-Mar-2023 Shift-3]",
        "options": ["Kerala", "Maharashtra", "Andhra Pradesh", "Tamil Nadu"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Maharashtra is the leading and largest producer of cashew nuts in India."
    },
    {
        "question": "In which state of India is the Sundarbans National Park located?\n\n[SSC GD 17-Jan-2023 Shift-4]",
        "options": ["Odisha", "Assam", "West Bengal", "Bihar"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Sundarbans National Park is located in West Bengal, famous for Royal Bengal Tigers and mangrove forests."
    },
    {
        "question": "What is the name of the strait that separates India and Sri Lanka?\n\n[SSC MTS 10-May-2023 Shift-3]",
        "options": ["Palk Strait", "Malacca Strait", "Bering Strait", "10 Degree Channel"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 The Palk Strait separates India (Tamil Nadu) and the Mannar district of Sri Lanka."
    },
    {
        "question": "With what is the 'Pink Revolution' in India associated?\n\n[SSC CHSL 14-Mar-2023 Shift-1]",
        "options": ["Tomato production", "Prawn and Onion production", "Meat production", "Fertilizer production"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Pink Revolution is associated with the production of Prawns and Onions."
    },
    {
        "question": "On which river is the Hirakud Dam constructed?\n\n[SSC GD 25-Jan-2023 Shift-2]",
        "options": ["Ganga", "Godavari", "Mahanadi", "Krishna"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Hirakud Dam, built on the Mahanadi river in Odisha, is the longest dam in India."
    },
    {
        "question": "In which state is 'Panna', famous for diamond mines, located?\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["Rajasthan", "Madhya Pradesh", "Jharkhand", "Chhattisgarh"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Panna district of Madhya Pradesh is world-famous for its major diamond mines."
    },
    {
        "question": "Which is the largest freshwater lake in India?\n\n[SSC GD 03-Feb-2023 Shift-3]",
        "options": ["Chilika Lake", "Wular Lake", "Sambhar Lake", "Dal Lake"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Wular Lake, located in Jammu and Kashmir, is the largest freshwater lake in India."
    },
    {
        "question": "Which of the following states has the longest coastline in India?\n\n[SSC CHSL 17-Mar-2023 Shift-4]",
        "options": ["Maharashtra", "Tamil Nadu", "Gujarat", "Andhra Pradesh"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Gujarat has the longest coastline in India, measuring approximately 1600 km."
    }, 
    {
        "question": "भारत की किस नदी को 'बूढ़ी गंगा' या 'दक्षिण गंगा' कहा जाता है?\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["कृष्णा", "कावेरी", "गोदावरी", "नर्मदा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 गोदावरी प्रायद्वीपीय भारत की सबसे लंबी नदी है, जिसे दक्षिण गंगा भी कहते हैं।"
    },
    {
        "question": "कपास (Cotton) की खेती के लिए सबसे उपयुक्त मिट्टी कौन सी है?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["जलोढ़ मिट्टी", "काली मिट्टी", "लाल मिट्टी", "लेटराइट मिट्टी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 काली मिट्टी को 'रेगुर मिट्टी' भी कहा जाता है और यह कपास उगाने के लिए सबसे अच्छी होती है।"
    },
    {
        "question": "भारत का सबसे ऊँचा सीधा गुरुत्वीय बांध (Gravity Dam) कौन सा है?\n\n[SSC GD 16-Jan-2023 Shift-2]",
        "options": ["टिहरी बांध", "भाखड़ा बांध", "हीराकुड बांध", "नागार्जुन सागर"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 सतलुज नदी पर बना भाखड़ा बांध भारत का सबसे ऊँचा गुरुत्वीय बांध है।"
    },
    {
        "question": "विश्व का सबसे बड़ा नदी द्वीप (River Island) 'माजुली' किस नदी पर स्थित है?\n\n[SSC MTS 08-May-2023 Shift-3]",
        "options": ["गंगा", "ब्रह्मपुत्र", "सिंधु", "गोदावरी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 असम में ब्रह्मपुत्र नदी पर स्थित माजुली द्वीप विश्व का सबसे बड़ा नदी द्वीप है।"
    },
    {
        "question": "भारत का सबसे पुराना राष्ट्रीय उद्यान (National Park) कौन सा है?\n\n[SSC CHSL 11-Aug-2023 Shift-1]",
        "options": ["काजीरंगा", "जिम कॉर्बेट", "गिर राष्ट्रीय उद्यान", "कान्हा"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 उत्तराखंड में स्थित जिम कॉर्बेट (पूर्व नाम हेली नेशनल पार्क) भारत का पहला राष्ट्रीय उद्यान है।"
    },
    {
        "question": "भारत में सबसे अधिक जलोढ़ मिट्टी (Alluvial Soil) किस क्षेत्र में पाई जाती है?\n\n[SSC GD 24-Jan-2023 Shift-1]",
        "options": ["उत्तरी मैदान", "दक्कन का पठार", "तटीय क्षेत्र", "थार मरुस्थल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 नदियों द्वारा बहाकर लाई गई जलोढ़ मिट्टी भारत के विशाल उत्तरी मैदानों में सबसे ज्यादा पाई जाती है।"
    },
    {
        "question": "जोग जलप्रपात (Jog Falls) भारत के किस राज्य में स्थित है?\n\n[SSC MTS 15-Jun-2023 Shift-3]",
        "options": ["केरल", "कर्नाटक", "तमिलनाडु", "महाराष्ट्र"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 शरावती नदी पर बना जोग प्रपात कर्नाटक राज्य में स्थित है।"
    },
    {
        "question": "क्षेत्रफल के अनुसार विश्व में भारत का कौन सा स्थान है?\n\n[SSC GD 02-Feb-2023 Shift-4]",
        "options": ["पांचवां", "छठा", "सातवां", "आठवां"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 क्षेत्रफल में भारत दुनिया का सातवां सबसे बड़ा देश है, जबकि रूस पहले स्थान पर है।"
    },
    {
        "question": "जादूगोड़ा (Jaduguda) की खानें किस खनिज के लिए प्रसिद्ध हैं?\n\n[SSC CHSL 17-Mar-2023 Shift-2]",
        "options": ["लोहा", "कोयला", "युरेनियम", "तांबा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 झारखंड के सिंहभूम जिले में स्थित जादूगोड़ा की खानें यूरेनियम खनन के लिए प्रसिद्ध हैं।"
    },
    {
        "question": "Which planet in our solar system is known as the 'Red Planet'?\n\n[SSC GD 11-Jan-2023 Shift-3]",
        "options": ["Venus", "Mercury", "Mars", "Jupiter"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Mars is called the Red Planet due to the abundance of iron oxide on its surface."
    },
    {
        "question": "Which river in India is also known as 'Dakshin Ganga' or 'Old Ganga'?\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["Krishna", "Kaveri", "Godavari", "Narmada"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Godavari is the longest river in peninsular India and is also called Dakshin Ganga."
    },
    {
        "question": "Which soil is most suitable for the cultivation of cotton?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["Alluvial Soil", "Black Soil", "Red Soil", "Laterite Soil"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Black soil is also known as 'Regur Soil' and is excellent for growing cotton crops."
    },
    {
        "question": "Which is the highest straight gravity dam in India?\n\n[SSC GD 16-Jan-2023 Shift-2]",
        "options": ["Tehri Dam", "Bhakra Dam", "Hirakud Dam", "Nagarjuna Sagar"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Bhakra Dam, built on the Sutlej river, is the highest gravity dam in India."
    },
    {
        "question": "The world's largest river island 'Majuli' is located on which river?\n\n[SSC MTS 08-May-2023 Shift-3]",
        "options": ["Ganga", "Brahmaputra", "Indus", "Godavari"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Majuli island, located on the Brahmaputra river in Assam, is the largest river island in the world."
    },
    {
        "question": "Which is the oldest National Park in India?\n\n[SSC CHSL 11-Aug-2023 Shift-1]",
        "options": ["Kaziranga", "Jim Corbett", "Gir National Park", "Kanha"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Jim Corbett National Park in Uttarakhand (formerly Hailey National Park) is the first national park in India."
    },
    {
        "question": "In which region of India is Alluvial Soil most widely found?\n\n[SSC GD 24-Jan-2023 Shift-1]",
        "options": ["Northern Plains", "Deccan Plateau", "Coastal Areas", "Thar Desert"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Alluvial soil brought down by rivers is most abundantly found in the vast Northern Plains of India."
    },
    {
        "question": "In which state of India is the Jog Waterfalls located?\n\n[SSC MTS 15-Jun-2023 Shift-3]",
        "options": ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Jog Falls is built on the Sharavati river and is located in the state of Karnataka."
    },
    {
        "question": "What is the rank of India in the world in terms of area?\n\n[SSC GD 02-Feb-2023 Shift-4]",
        "options": ["5th", "6th", "7th", "8th"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 India is the 7th largest country in the world by area, while Russia holds the first position."
    },
    {
        "question": "The mines of Jaduguda are famous for which of the following minerals?\n\n[SSC CHSL 17-Mar-2023 Shift-2]",
        "options": ["Iron", "Coal", "Uranium", "Copper"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Jaduguda mines, located in the Singhbhum district of Jharkhand, are famous for Uranium mining."
    }

]
