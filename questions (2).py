# 📚 टेलीग्राम क्विज़ बॉट प्रश्न बैंक (Question Bank) - भाग 1

QUIZ_LIST = [
    # =====================================================
    # ------------------- HINDI QUIZZES -------------------
    # =====================================================
    {
        "question": "भारत के किस स्थान पर विश्व की सबसे अधिक औसत वार्षिक वर्षा दर्ज की जाती है?\n\n[SSC CGL]",
        "options": ["चेरापूंजी", "मासिनराम (Mawsynram)", "अगुम्बे", "महाबलेश्वर"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 मेघालय की खासी पहाड़ियों में स्थित मासिनराम (Mawsynram) में बंगाल की खाड़ी के मानसून के फंसने (कीपाकार पहाड़ियों) के कारण दुनिया की सबसे ज्यादा बारिश होती है।"
    },
    {
        "question": "निम्नलिखित कथनों पर विचार कीजिए:\n1. शिवालिक के पास नदियाँ पहाड़ों से नीचे उतरते समय 'भाबर' क्षेत्र में विलीन हो जाती हैं।\n2. 'तराई' क्षेत्र भाबर के दक्षिण में स्थित है जहाँ नदियाँ पुनः प्रकट होकर दलदली क्षेत्र बनाती हैं।\n\nउपरोक्त में से कौन सा/से कथन सत्य है/हैं?\n\n[UPSC CSE]",
        "options": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भाबर क्षेत्र पत्थरों और कंकड़ों से बना है जहाँ नदियाँ भूमिगत हो जाती हैं। इसके ठीक दक्षिण में तराई क्षेत्र है जहाँ यह पानी सतह पर आकर घने जंगलों और दलदल का निर्माण करता है।"
    },
    {
        "question": "करेवा (Karewas) भू-आकृतियाँ, जो मुख्य रूप से ज़ाफरान (केसर) की खेती के लिए प्रसिद्ध हैं, हिमालय के किस भाग में पाई जाती हैं?\n\n[UPSC CSE]",
        "options": ["कुमाऊँ हिमालय", "कश्मीर हिमालय", "नेपाल हिमालय", "असम हिमालय"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 करेवा कश्मीरी हिमालय में पाए जाने वाले हिमनद (Glacial) मिट्टी और अन्य सामग्रियों के मोटे जमाव (Terraces) हैं, जो उच्च गुणवत्ता वाले केसर की खेती के लिए अत्यधिक उपजाऊ होते हैं।"
    },
    {
        "question": "भारत के पश्चिमी तट पर होने वाली मानसूनी वर्षा के संदर्भ में 'घाटियों का हवादार होना' (Orographic Rain) मुख्य कारण है। पश्चिमी घाट के संदर्भ में पालघाट दर्रा (Palghat Gap) तमिलनाडु के आंतरिक भागों में वर्षा को कैसे प्रभावित करता है?\n\n[UPPSC Poly]",
        "options": ["यह मानसूनी हवाओं को रोकता है जिससे तमिलनाडु शुष्क रहता है", "यह अरब सागर की मानसूनी शाखा को पार जाने देता है जिससे आंतरिक भागों में वर्षा होती है", "यह चक्रवातों को आकर्षित करता है", "यह वर्षा पर कोई प्रभाव नहीं डालता"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 पालघाट दर्रा पश्चिमी घाट में एक बड़ा गैप (दरार) है। इसके माध्यम से अरब सागर से आने वाली दक्षिण-पश्चिम मानसून की हवाएँ आसानी से पार होकर तमिलनाडु के कोयंबटूर और आस-पास के आंतरिक क्षेत्रों में वर्षा कराती हैं।"
    },
    {
        "question": "नदियों के उद्गम के संदर्भ में निम्नलिखित युग्मों पर विचार कीजिए:\n1. रुद्रप्रयाग - अलकनंदा और मंदाकिनी का संगम\n2. कर्णप्रयाग - अलकनंदा और पिंडार का संगम\n3. देवप्रयाग - भागीरथी और अलकनंदा का संगम\n\nइनमें से कौन से युग्म सही सुमेलित हैं?\n\n[UPSC CSE]",
        "options": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3 सभी"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 उत्तराखंड के पंच प्रयाग में ये सभी सुमेलित हैं। देवप्रयाग के बाद ही संयुक्त धारा को 'गंगा' नदी के नाम से जाना जाता है।"
    },
    {
        "question": "भारत में पाई जाने वाली 'लैटेराइट मिट्टी' (Laterite Soil) के निर्माण के लिए कौन सी जलवायु परिस्थितियाँ अनिवार्य हैं?\n\n[BPSC High Level]",
        "options": ["अत्यधिक शीत और शुष्क जलवायु", "कम वर्षा और उच्च तापमान", "तीव्र निक्षालन (Leaching) के साथ उच्च तापमान और भारी मौसमी वर्षा", "अर्ध-शुष्क और रेतीली जलवायु"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 लैटेराइट मिट्टी का निर्माण भारी वर्षा के कारण होने वाले तीव्र निक्षालन (Leaching) की वजह से होता है, जिससे मिट्टी के पोषक तत्व और सिलिका बह जाते हैं और केवल लोहा व एल्युमिनियम के ऑक्साइड बचते हैं।"
    },
    {
        "question": "अंडमान और निकोबार द्वीप समूह को अलग करने वाले 'दस डिग्री चैनल' (10 Degree Channel) के उत्तर और दक्षिण में क्रमशः कौन से द्वीप स्थित हैं?\n\n[UPSC CSE]",
        "options": ["उत्तरी अंडमान और मध्य अंडमान", "दक्षिण अंडमान और लिटिल अंडमान", "लिटिल अंडमान और कार निकोबार", "कार निकोबार और ग्रेट निकोबार"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 10 डिग्री चैनल (10° N अक्षांश) बंगाल की खाड़ी में स्थित है जो उत्तर में 'लिटिल अंडमान' को दक्षिण में 'कार निकोबार' से भौगोलिक रूप से अलग करता है।"
    },
    {
        "question": "निम्नलिखित कथनों पर विचार कीजिए:\n1. भारत का प्रायद्वीपीय पठार (Peninsular Plateau) गोंडवाना भूमि का हिस्सा है और यह देश का सबसे प्राचीन भूभाग है।\n2. अरावली पर्वत शृंखला विश्व की सबसे पुरानी वलित (Fold) पर्वत शृंखलाओं में से एक है जो अब एक अवशिष्ट (Residual) पर्वत है।\n\nसही कथन चुनिए:\n\n[RAS / RPSC]",
        "options": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 दोनों कथन सत्य हैं। प्रायद्वीपीय पठार पृथ्वी की पपड़ी के सबसे स्थिर और पुराने हिस्सों में से एक है। अरावली कभी विशाल वलित पर्वत था, जो समय के साथ अपक्षय के कारण अब अवशिष्ट मात्र रह गया है।"
    },
    {
        "question": "यदि आप भारत के एक छोर 'गुहार मोती' (गुजरात) से दूसरे छोर 'किबिथु' (अरुणाचल प्रदेश) की यात्रा करते हैं, तो दोनों स्थानों के स्थानीय समयानुसार सूर्योदय में लगभग कितने समय का अंतर होगा?\n\n[UPSC Capf]",
        "options": ["लगभग 30 मिनट", "लगभग 1 घंटा", "लगभग 2 घंटे", "लगभग 3 घंटे"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भारत का देशांतरीय विस्तार लगभग 30° है (68°7' E से 97°25' E)। चूंकि 1° देशांतर पार करने में 4 मिनट का समय लगता है, इसलिए 30 × 4 = 120 मिनट यानी लगभग 2 घंटे का अंतर आता है।"
    },
    {
        "question": "प्रायद्वीपीय भारत की पूर्व की ओर बहने वाली नदियों (जैसे गोदावरी, कृष्णा) के मुहाने पर विशाल डेल्टा बनते हैं, जबकि पश्चिमी तट पर बहने वाली नदियाँ (जैसे नर्मदा, तापी) डेल्टा के बजाय ज्वारनदमुख (Estuary) बनाती हैं। इसका मुख्य कारण क्या है?\n\n[UPSC CSE]",
        "options": ["पश्चिमी नदियाँ बहुत लंबी हैं", "पश्चिमी घाट तीव्र ढाल वाले हैं और नदियाँ कठोर चट्टानों से होकर बहती हैं जिससे गाद (Sediment) नहीं बचती", "पूर्वी नदियाँ अरब सागर में गिरती हैं", "पश्चिमी तट पर वर्षा बहुत कम होती है"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 पश्चिमी घाट की ढलान बहुत तीव्र है जिससे नदियाँ अत्यधिक तीव्र गति से बहती हैं और कठोर चट्टानी रास्तों के कारण अपने साथ गाद या मलबा नहीं ला पातीं, जिससे डेल्टा का निर्माण संभव नहीं हो पाता।"
    },
    {
        "question": "दक्कन ट्रैप (Deccan Trap) की बेसाल्टिक लावा चट्टानों का निर्माण मुख्य रूप से भूवैज्ञानिक समय पैमाने (Geological Time Scale) के किस काल/युग में हुआ था?\n\n[UPSC Geo-Scientist]",
        "options": ["कैम्ब्रियन काल", "क्रेटेशियस काल (Cretaceous Period)", "कार्बोनिफेरस काल", "प्लीस्टोसिन युग"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 दक्कन ट्रैप के विशाल बेसाल्ट लावा पठार का निर्माण मेसोजोइक महाकल्प के अंत में, मुख्य रूप से क्रेटेशियस काल (लगभग 66-60 मिलियन वर्ष पहले) के दौरान ज्वालामुखीय विदर उद्भेदन (Fissure Eruption) से हुआ था।"
    },
    {
        "question": "शेरशाह सूरी के प्रशासनिक सुधारों के संदर्भ में 'दाम' और 'रुपया' क्रमशः किन धातुओं के सिक्के थे?\n\n[UPPSC]",
        "options": ["सोना और चांदी", "चांदी और तांबा", "तांबा और चांदी", "सोना और तांबा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 शेरशाह सूरी ने मुद्रा व्यवस्था में व्यापक सुधार किए। उसने तांबे का सिक्का चलाया जिसे 'दाम' कहा जाता था और चांदी का सिक्का चलाया जिसे 'रुपया' (178 ग्रेन) कहा जाता था। यही रुपया आधुनिक भारतीय मुद्रा का आधार बना।"
    },
    {
        "question": "1857 के विद्रोह के ठीक बाद बंगाल में निम्नलिखित में से कौन सा प्रसिद्ध व्यवधान या विद्रोह हुआ था?\n\n[UPSC CSE]",
        "options": ["संथाल विद्रोह", "पबना विद्रोह", "नील विद्रोह (Indigo Revolt)", "सन्यासी विद्रोह"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 वर्ष 1859-60 में बंगाल में नील विद्रोह हुआ, जहाँ किसानों ने जबरन नील की खेती कराए जाने के खिलाफ आंदोलन किया। दीनबंधु मित्र ने अपने नाटक 'नील दर्पण' में इस क्रूरता को दर्शाया था। (संथाल विद्रोह 1855-56 में यानी 1857 से पहले हुआ था)।"
    },
    {
        "question": "वर्ष 1905 में लॉर्ड कर्जन द्वारा किए गए बंगाल विभाजन को किस वर्ष और किस वायसराय के कार्यकाल के दौरान रद्द किया गया था?\n\n[WB Civil Services]",
        "options": ["1911 - लॉर्ड हार्डिंग द्वितीय", "1909 - लॉर्ड मिन्टो", "1912 - लॉर्ड चेम्सफोर्ड", "1915 - लॉर्ड हार्डिंग"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 ब्रिटिश सम्राट जॉर्ज पंचम के भारत आगमन पर दिसंबर 1911 में दिल्ली दरबार का आयोजन किया गया था। इसी दौरान वायसराय लॉर्ड हार्डिंग द्वितीय के कार्यकाल में बंगाल विभाजन को रद्द करने और भारत की राजधानी कोलकाता से दिल्ली स्थानांतरित करने की घोषणा की गई थी।"
    },
    {
        "question": "1916 के ऐतिहासिक 'लखनऊ समझौते' (Lucknow Pact) की मुख्य विशेषता क्या थी?\n\n[UPSC CSE]",
        "options": ["कांग्रेस ने मुस्लिम लीग की अलग निर्वाचन मंडल (Separate Electrorate) की मांग को स्वीकार कर लिया और कांग्रेस के दोनों धड़ों (नरम दल और गरम दल) का पुनर्मिलन हुआ", "मुस्लिम लीग का कांग्रेस में पूर्ण विलय हो गया", "कांग्रेस ने पूर्ण स्वराज की मांग छोड़ दी", "वायसराय की कार्यकारी परिषद का पूर्ण बहिष्कार किया गया"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 अंबिका चरण मजूमदार की अध्यक्षता में हुए लखनऊ अधिवेशन में बाल गंगाधर तिलक और एनी बेसेंट के प्रयासों से नरम दल और गरम दल एक हुए। साथ ही, कांग्रेस और मुस्लिम लीग के बीच समझौता हुआ, जिसमें कांग्रेस ने पहली बार मुस्लिमों के लिए पृथक निर्वाचन की मांग को मान लिया, जिसे दूरगामी रूप से एक ऐतिहासिक भूल भी कहा जाता है।"
    },
    # =====================================================
    # ----------- GROUP 1: CONSTITUTIONAL FRAMEWORK -------
    # =====================================================
    {
        "question": "निम्नलिखित कथनों पर विचार कीजिए:\n1. भारत के संविधान की प्रस्तावना (Preamble) संविधान का एक भाग है लेकिन इसका कोई कानूनी प्रभाव नहीं है।\n2. प्रस्तावना में 'समाजवादी' और 'पंथनिरपेक्ष' शब्द मूल संविधान का हिस्सा थे।\n\nसही कथन चुनिए:\n\n[UPSC CSE]",
        "options": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 केशवानंद भारती मामले (1973) में सुप्रीम कोर्ट ने माना कि प्रस्तावना संविधान का हिस्सा है। हालांकि, अन्य भागों से स्वतंत्र इसका कोई अलग कानूनी प्रभाव नहीं है। 'समाजवादी' और 'पंथनिरपेक्ष' शब्द 42वें संशोधन (1976) द्वारा जोड़े गए थे।"
    },
    {
        "question": "भारतीय संविधान की 9वीं अनुसूची (9th Schedule) को किस प्रधानमंत्री के कार्यकाल के दौरान शामिल किया गया था?\n\n[UPSC CSE]",
        "options": ["जवाहरलाल नेहरू", "लाल बहादुर शास्त्री", "इन्दिरा गांधी", "मोरारजी देसाई"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 प्रथम संविधान संशोधन अधिनियम, 1951 के माध्यम से संविधान में 9वीं अनुसूची जोड़ी गई थी। उस समय भारत के प्रधानमंत्री जवाहरलाल नेहरू थे। इसका उद्देश्य भूमि सुधार कानूनों को न्यायिक समीक्षा से बचाना था।"
    },
    {
        "question": "भारत के संविधान का कौन सा अनुच्छेद अपनी पसंद के व्यक्ति से विवाह करने के किसी व्यक्ति के अधिकार को संरक्षण देता है?\n\n[UPSC CSE]",
        "options": ["अनुच्छेद 19", "अनुच्छेद 21", "अनुच्छेद 25", "अनुच्छेद 29"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 उच्चतम न्यायालय ने 'शफीन जहां बनाम के.एम. अशोकन (2018)' मामले (हादिया केस) में यह दोहराया कि अपनी पसंद के व्यक्ति से शादी करने का अधिकार अनुच्छेद 21 के तहत जीवन और व्यक्तिगत स्वतंत्रता के अधिकार का एक अभिन्न अंग है।"
    },
    {
        "question": "निवारक निरोध (Preventive Detention) के अंतर्गत एक व्यक्ति को बिना मुकदमा चलाए अधिकतम कितने समय तक हिरासत में रखा जा सकता है, यदि सलाहकार बोर्ड अवधि बढ़ाने की सिफारिश न करे?\n\n[UPPSC]",
        "options": ["1 महीना", "2 महीने", "3 महीने", "6 महीने"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 22(4) के तहत, निवारक निरोध कानून के अंतर्गत किसी व्यक्ति को अधिकतम 3 महीने तक ही हिरासत में रखा जा सकता है। इससे अधिक समय के लिए सलाहकार बोर्ड (Advisory Board) की समीक्षा और अनुमति अनिवार्य होती है।"
    },
    {
        "question": "निम्नलिखित में से कौन सा नीति निदेशक तत्व (DPSP) मूल संविधान में नहीं था बल्कि बाद में संशोधन द्वारा जोड़ा गया?\n\n[BPSC]",
        "options": ["ग्राम पंचायतों का गठन", "समान नागरिक संहिता", "उद्योगों के प्रबंधन में श्रमिकों की भागीदारी", "कृषि और पशुपालन का संगठन"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 43A (उद्योगों के प्रबंधन में श्रमिकों की भागीदारी) को 42वें संविधान संशोधन अधिनियम, 1976 द्वारा जोड़ा गया था। बाकी तीनों विकल्प मूल संविधान में पहले से मौजूद थे।"
    },
    # =====================================================
    # ----------- GROUP 2: UNION EXECUTIVE & PARLIAMENT ---
    # =====================================================
    {
        "question": "भारत के राष्ट्रपति के महाभियोग (Impeachment) के संदर्भ में कौन सा कथन सत्य है?\n\n[UPSC CSE]",
        "options": ["संसद के दोनों सदनों के नामांकित सदस्य (Nominated Members) इसमें भाग नहीं ले सकते", "राज्यों की विधानसभाओं के निर्वाचित सदस्य इसमें भाग लेते हैं", "महाभियोग का प्रस्ताव केवल लोकसभा में ही पेश किया जा सकता है", "संसद के दोनों सदनों के नामांकित सदस्य इस प्रक्रिया में भाग ले सकते हैं"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 राष्ट्रपति के चुनाव में संसद के नामांकित सदस्य वोट नहीं देते, लेकिन महाभियोग (अनुच्छेद 61) की प्रक्रिया में वे भाग लेते हैं। इसके विपरीत, राज्यों की विधानसभाओं के सदस्य चुनाव में भाग लेते हैं लेकिन महाभियोग में नहीं।"
    },
    {
        "question": "यदि भारत के प्रधानमंत्री संसद के उच्च सदन (राज्यसभा) के सदस्य हैं, तो:\n\n[UPSC CSE]",
        "options": ["वे अविश्वास प्रस्ताव (No-Confidence Motion) की स्थिति में अपने पक्ष में वोट नहीं दे सकेंगे", "वे निम्न सदन में बजट पर नहीं बोल सकेंगे", "वे केवल उच्च सदन में ही वक्तव्य दे सकते हैं", "उन्हें छह महीने के भीतर लोकसभा की सदस्यता लेनी होगी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 अविश्वास प्रस्ताव केवल लोकसभा में लाया और पास किया जाता है। चूंकि प्रधानमंत्री राज्यसभा के सदस्य हैं, इसलिए वे लोकसभा की वोटिंग में हिस्सा नहीं ले सकते, भले ही प्रस्ताव उनकी सरकार के खिलाफ हो।"
    },
    {
        "question": "संसद में 'निंदा प्रस्ताव' (Censure Motion) और 'अविश्वास प्रस्ताव' (No-Confidence Motion) के बीच मुख्य अंतर क्या है?\n\n[MPSC]",
        "options": ["निंदा प्रस्ताव केवल पूरे मंत्रिपरिषद के खिलाफ लाया जा सकता है", "अविश्वास प्रस्ताव लाने के लिए लोकसभा में इसके कारण बताना अनिवार्य है", "निंदा प्रस्ताव को स्वीकार करने के कारण बताना आवश्यक है, जबकि अविश्वास प्रस्ताव के लिए ऐसा आवश्यक नहीं है", "दोनों प्रस्तावों के पारित होने पर सरकार को इस्तीफा देना पड़ता है"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 लोकसभा के नियमों के तहत, निंदा प्रस्ताव लाने के कारण स्पष्ट करने होते हैं और यह किसी एक मंत्री या पूरी मंत्रिपरिषद के खिलाफ हो सकता है। इसके विपरीत, अविश्वास प्रस्ताव के लिए कोई कारण बताना जरूरी नहीं होता और इसके पास होने पर सरकार गिर जाती है।"
    },
    {
        "question": "संसद के दोनों सदनों की संयुक्त बैठक (Joint Sitting) की अध्यक्षता लोकसभा अध्यक्ष की अनुपस्थिति में कौन करता है?\n\n[RAS / RPSC]",
        "options": ["भारत का उपराष्ट्रपति", "राज्यसभा का उपसभापति (Deputy Chairman)", "राज्यसभा का सभापति", "संसद का वरिष्ठतम सदस्य"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 यदि लोकसभा अध्यक्ष अनुपस्थित हैं, तो उपाध्यक्ष (Deputy Speaker) अध्यक्षता करते हैं। यदि वे भी अनुपस्थित हों, तो राज्यसभा के उपसभापति (Deputy Chairman) अध्यक्षता करते हैं। राज्यसभा के सभापति (उपराष्ट्रपति) कभी भी संयुक्त बैठक की अध्यक्षता नहीं करते क्योंकि वे संसद के किसी सदन के सदस्य नहीं होते।"
    },
    {
        "question": "संविधान के किस अनुच्छेद के तहत संसद को राज्य सूची (State List) के विषयों पर राष्ट्रीय हित में कानून बनाने की शक्ति प्राप्त है?\n\n[UPSC CSE]",
        "options": ["अनुच्छेद 249", "अनुच्छेद 250", "अनुच्छेद 252", "अनुच्छेद 253"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 249 के तहत यदि राज्यसभा दो-तिहाई बहुमत से यह प्रस्ताव पारित कर दे कि राज्य सूची का कोई विषय राष्ट्रीय महत्व का है, तो संसद उस पर कानून बना सकती है। यह कानून एक बार में अधिकतम 1 वर्ष के लिए प्रभावी होता है।"
    },
    # =====================================================
    # ----------- GROUP 3: JUDICIARY & FEDERALISM ----------
    # =====================================================
    {
        "question": "संविधान के 'मूल ढांचे' (Basic Structure) के सिद्धांत का प्रतिपादन सर्वोच्च न्यायालय ने किस ऐतिहासिक मामले में किया था?\n\n[WBCS]",
        "options": ["गोलकनाथ मामला (1967)", "केशवानंद भारती मामला (1973)", "मिनर्वा मिल्स मामला (1980)", "ए.के. गोपालन मामला (1950)"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 24 अप्रैल 1973 को केशवानंद भारती बनाम केरल राज्य मामले में 13 जजों की सबसे बड़ी पीठ ने 7:6 के बहुमत से फैसला सुनाते हुए 'मूल ढांचे' का सिद्धांत दिया, जिसके तहत संसद संविधान के मौलिक स्वरूप को नहीं बदल सकती।"
    },
    {
        "question": "भारत के सर्वोच्च न्यायालय के पास 'मूल क्षेत्राधिकार' (Original Jurisdiction) के तहत किस प्रकार के विवाद आते हैं?\n\n[UPSC CSE]",
        "options": ["दीवानी और आपराधिक मामले", "संसद सदस्यों के चुनाव से जुड़े विवाद", "भारत सरकार और एक या अधिक राज्यों के बीच के विवाद", "संवैधानिक व्याख्या से जुड़े अपील मामले"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अनुच्छेद 131 के तहत संघीय ढांचे के विवाद (जैसे केंद्र बनाम राज्य, या राज्य बनाम राज्य) सीधे सर्वोच्च न्यायालय के मूल क्षेत्राधिकार में आते हैं। इनकी शुरुआत किसी अन्य निचली अदालत में नहीं की जा सकती।"
    },
    {
        "question": "उच्च न्यायालय (High Court) के न्यायाधीशों के वेतन और भत्ते तथा उनकी पेंशन क्रमशः कहाँ से दी जाती है?\n\n[UPPSC]",
        "options": ["दोनों भारत की संचित निधि से", "दोनों राज्य की संचित निधि से", "वेतन-भत्ते राज्य की संचित निधि से और पेंशन भारत की संचित निधि से", "वेतन-भत्ते भारत की संचित निधि से और पेंशन राज्य की संचित निधि से"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 हाईकोर्ट के जजों को कार्यकाल के दौरान वेतन और भत्ते संबंधित राज्य की संचित निधि (Consolidated Fund of State) से मिलते हैं, लेकिन उनकी पेंशन भारत की संचित निधि (Consolidated Fund of India) पर भारित होती है।"
    },
    {
        "question": "सरकारी आयोग (Sarkaria Commission) और पुंछी आयोग (Punchhi Commission) का गठन संविधान के किस आयाम की समीक्षा के लिए किया गया था?\n\n[UPSC CSE]",
        "options": ["न्यायिक सक्रियता", "केंद्र-राज्य संबंध (Center-State Relations)", "चुनावी सुधार", "मूल अधिकार और नीति निदेशक तत्व"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 सरकारी आयोग (1983) और मदन मोहन पुंछी आयोग (2007) दोनों का गठन भारत में केंद्र और राज्यों के बीच शक्ति के संतुलन, राज्यपाल की भूमिका और वित्तीय संबंधों की समीक्षा व सुधार के लिए किया गया था।"
    },
    # =====================================================
    # ---------------- HISTORY QUIZZES (PART 1) -----------
    # =====================================================
    {
        "question": "सिंधु घाटी सभ्यता के किस स्थल से 'अग्निकुंड/अग्नि वेदिकाओं' (Fire Altars) के साक्ष्य मिले हैं, जो वहां अनुष्ठानिक प्रथाओं को दर्शाते हैं?\n\n[UPSC CSE]",
        "options": ["मोहनजोदड़ो", "कालीबंगा (और लोथल)", "चन्हूदड़ो", "बनावली"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 राजस्थान के कालीबंगा और गुजरात के लोथल से मिट्टी के चबूतरों पर कतारबद्ध अग्निकुंड या यज्ञ वेदिकाओं के साक्ष्य मिले हैं, जो यह संकेत देते हैं कि वहां के लोग अग्नि पूजा या यज्ञ जैसे अनुष्ठान करते थे।"
    },
    {
        "question": "प्राचीन बौद्ध दर्शन के संदर्भ में 'महायान' और 'हीनयान' संप्रदायों के बीच मुख्य अंतर क्या था?\n\n[UPPSC]",
        "options": ["हीनयान बुद्ध को भगवान मानता था, जबकि महायान उन्हें केवल एक शिक्षक मानता था", "महायान में बुद्ध की मूर्ति पूजा और बोधिसत्व की अवधारणा केंद्रीय थी, जबकि हीनयान ने बुद्ध के मूल प्रतीकात्मक रूप को बनाए रखा", "हीनयान संस्कृत का प्रयोग करता था, जबकि महायान पालि भाषा का", "दोनों में कोई दार्शनिक अंतर नहीं था"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 कनिष्क के काल में चौथी बौद्ध संगीति के दौरान बौद्ध धर्म दो भागों में बंटा। महायान संप्रदाय ने बुद्ध को भगवान मानकर उनकी मूर्तियां बनाना और बोधिसत्व (दूसरों के कल्याण के लिए काम करने वाले) की पूजा करना शुरू किया, जबकि हीनयान आत्म-अनुशासन और ध्यान पर जोर देता था।"
    },
    {
        "question": "अशोक के अभिलेखों को सर्वप्रथम पढ़ने में सफलता किस विद्वान को मिली थी और यह किस वर्ष हुआ था?\n\n[BPSC]",
        "options": ["विलियम जोन्स (1784)", "जेम्स प्रिंसेप (1837)", "चार्ल्स विल्किन्स (1785)", "मैक्स मूर (1850)"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 ईस्ट इंडिया कंपनी के अधिकारी और प्राच्यविद जेम्स प्रिंसेप ने 1837 में पहली बार अशोक के ब्राह्मी लिपि में लिखे अभिलेखों को पढ़ा और स्पष्ट किया कि इनमें 'देवानांपिय पियदसी' शब्द सम्राट अशोक के लिए प्रयुक्त हुआ है।"
    },
    {
        "question": "गुप्त काल के दौरान लिखे गए प्रसिद्ध संस्कृत नाटक 'मृच्छकटिकम्' (The Little Clay Cart) के लेखक कौन थे?\n\n[UPSC CSE]",
        "options": ["कालिदास", "विशाखदत्त", "शूद्रक", "भारवि"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 'मृच्छकटिकम्' की रचना महाकवि शूद्रक ने की थी। यह नाटक एक गरीब ब्राह्मण चारुदत्त और एक अमीर गणिका वसंतसेना की प्रेम कहानी पर आधारित है, जो गुप्तकालीन समाज की सामाजिक और आर्थिक स्थिति का सटीक चित्रण करता है।"
    },
    {
        "question": "विजयनगर साम्राज्य के किस राजा के दरबार को 'अष्टदिग्गज' (आठ महान तेलुगु कवि) सुशोभित करते थे?\n\n[RAS / RPSC]",
        "options": ["हरिहर प्रथम", "देवराय द्वितीय", "कृष्णदेव राय", "अच्युत देव राय"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 तुलुव वंश के प्रतापी राजा कृष्णदेव राय (1509-1529) का काल तेलुगु साहित्य का स्वर्ण युग माना जाता है। उनके दरबार में आठ सर्वोत्कृष्ट कवि थे जिन्हें 'अष्टदिग्गज' कहा जाता था, जिनमें अल्लसानी पेद्दन और तेनालीराम प्रमुख थे।"
    },
    {
        "question": "दिल्ली सल्तनत के किस सुल्तान ने 'बाजार नियंत्रण और मूल्य निर्धारण प्रणाली' (Market Control System) को कड़ाई से लागू किया था?\n\n[UPSC CDS]",
        "options": ["इल्तुतमिश", "बलबन", "अलाउद्दीन खिलजी", "मोहम्मद बिन तुगलक"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अलाउद्दीन खिलजी ने एक विशाल स्थायी सेना को कम वेतन में बनाए रखने के लिए यह प्रणाली शुरू की थी। उसने अनाज, कपड़ों और मवेशियों तक के दाम तय कर दिए थे और इसकी निगरानी के लिए 'शहना-ए-मंडी' नामक अधिकारी नियुक्त किया था।"
    },
    {
        "question": "सिंधु घाटी सभ्यता का प्रसिद्ध स्थल 'कालीबंगा' वर्तमान में किस राज्य में स्थित है?\n\n[SSC GD 12-Jan-2023 Shift-2]",
        "options": ["गुजरात", "पंजाब", "राजस्थान", "हरियाणा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 कालीबंगा राजस्थान के हनुमानगढ़ जिले में घग्गर नदी के किनारे स्थित है। यहाँ से जुते हुए खेतों के साक्ष्य मिले हैं।"
    },
    {
        "question": "गौतम बुद्ध के बचपन का नाम क्या था?\n\n[SSC MTS 04-May-2023 Shift-1]",
        "options": ["सिद्धार्थ", "वर्धमान", "राहुल", "देवदत्त"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 महात्मा बुद्ध के बचपन का नाम सिद्धार्थ था, जबकि महावीर स्वामी के बचपन का नाम वर्धमान था।"
    },
    {
        "question": "मौर्य साम्राज्य का अंतिम शासक कौन था?\n\n[SSC CHSL 16-Mar-2023 Shift-3]",
        "options": ["चंद्रगुप्त मौर्य", "बिन्दुसार", "दशरथ", "बृहद्रथ"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 मौर्य वंश का अंतिम शासक बृहद्रथ था, जिसकी हत्या उसके सेनापति पुष्यमित्र शुंग ने करके शुंग वंश की स्थापना की थी।"
    },
    {
        "question": "गुप्त वंश का संस्थापक कौन था?\n\n[SSC GD 17-Jan-2023 Shift-1]",
        "options": ["चंद्रगुप्त प्रथम", "श्रीगुप्त", "समुद्रगुप्त", "घटोत्कच"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 गुप्त साम्राज्य की स्थापना महाराजा श्रीगुप्त ने लगभग 275 ईस्वी में की थी।"
    },
    {
        "question": "आगरा शहर की स्थापना 1504 ई. में किस सुल्तान ने की थी?\n\n[SSC MTS 11-May-2023 Shift-3]",
        "options": ["बहलोल लोदी", "सिकंदर लोदी", "इब्राहिम लोदी", "खिज्र खान"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 सिकंदर लोदी ने 1504 में आगरा शहर बसाया था और बाद में इसे दिल्ली सल्तनत की राजधानी बनाया था।"
    },
    {
        "question": "किस मुगल शासक को 'जिंदा पीर' (Living Saint) कहा जाता था?\n\n[SSC CHSL 13-Mar-2023 Shift-4]",
        "options": ["अकबर", "जहाँगीर", "शाहजहाँ", "औरंगज़ेब"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 अपने सादा जीवन और धार्मिक कट्टरता के कारण औरंगज़ेब को इतिहास में 'जिंदा पीर' कहा जाता था।"
    },
    {
        "question": "प्रसिद्ध 'दीन-ए-इलाही' धर्म की शुरुआत किस मुगल सम्राट ने की थी?\n\n[SSC GD 27-Jan-2023 Shift-4]",
        "options": ["बाबर", "हुमायूँ", "अकबर", "शाहजहाँ"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अकबर ने 1582 ई. में सभी धर्मों के मूल सिद्धांतों को मिलाकर 'दीन-ए-इलाही' नामक एक नया धर्म शुरू किया था।"
    },
    {
        "question": "कोलकाता में 'रामकृष्ण मिशन' की स्थापना 1897 में किसने की थी?\n\n[SSC MTS 16-Jun-2023 Shift-2]",
        "options": ["स्वामी विवेकानंद", "रामकृष्ण परमहंस", "स्वामी दयानंद सरस्वती", "देवेन्द्रनाथ टैगोर"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 स्वामी विवेकानंद ने अपने गुरु रामकृष्ण परमहंस की स्मृति और उनके संदेशों के प्रचार के लिए रामकृष्ण मिशन की स्थापना की थी।"
    },
    {
        "question": "बंगाल का विभाजन किस वर्ष और किस वायसराय के काल में हुआ था?\n\n[SSC GD 06-Feb-2023 Shift-1]",
        "options": ["1905, लॉर्ड कर्जन", "1911, लॉर्ड हार्डिंग", "1905, लॉर्ड मिंटो", "1919, लॉर्ड चेम्सफोर्ड"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 लॉर्ड कर्जन ने प्रशासनिक सुधारों का बहाना बनाकर 1905 में बंगाल का विभाजन (Partition of Bengal) कर दिया था।"
    },
    {
        "question": "गांधी जी ने 'करो या मरो' (Do or Die) का नारा किस आंदोलन के दौरान दिया था?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["असहयोग आंदोलन", "सविनय अवज्ञा आंदोलन", "भारत छोड़ो आंदोलन", "चंपारण सत्याग्रह"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 8 अगस्त 1942 को बम्बई के ग्वालिया टैंक मैदान से शुरू हुए 'भारत छोड़ो आंदोलन' में गांधी जी ने 'करो या मरो' का प्रसिद्ध नारा दिया था।"
    },
    {
        "question": "In which present-day state is 'Kalibangan', the famous site of the Indus Valley Civilization, located?\n\n[SSC GD 12-Jan-2023 Shift-2]",
        "options": ["Gujarat", "Punjab", "Rajasthan", "Haryana"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Kalibangan is located along the banks of the Ghaggar river in the Hanumangarh district of Rajasthan, famous for excavated ploughed fields."
    },
    {
        "question": "What was the childhood name of Gautam Buddha?\n\n[SSC MTS 04-May-2023 Shift-1]",
        "options": ["Siddhartha", "Vardhamana", "Rahul", "Devadatta"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 The childhood name of Mahatma Buddha was Siddhartha, while Vardhamana was the childhood name of Mahavira Swami."
    },
    {
        "question": "Who was the last ruler of the Mauryan Empire?\n\n[SSC CHSL 16-Mar-2023 Shift-3]",
        "options": ["Chandragupta Maurya", "Bindusara", "Dasharatha", "Brihadratha"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Brihadratha was the last ruler of the Mauryan dynasty. He was assassinated by his commander Pushyamitra Shunga, who founded the Shunga dynasty."
    },
    {
        "question": "Who was the founder of the Gupta Dynasty?\n\n[SSC GD 17-Jan-2023 Shift-1]",
        "options": ["Chandragupta I", "Sri Gupta", "Samudragupta", "Ghatotkacha"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Gupta Empire was founded by Maharaja Sri Gupta around 275 AD."
    },
    {
        "question": "Which sultan founded the city of Agra in 1504 AD?\n\n[SSC MTS 11-May-2023 Shift-3]",
        "options": ["Bahlul Lodi", "Sikandar Lodi", "Ibrahim Lodi", "Khizr Khan"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Sikandar Lodi founded the city of Agra in 1504 and later made it the official capital of the Delhi Sultanate."
    },
    {
        "question": "Which Mughal ruler was popularly known as 'Zinda Peir' (Living Saint)?\n\n[SSC CHSL 13-Mar-2023 Shift-4]",
        "options": ["Akbar", "Jahangir", "Shah Jahan", "Aurangzeb"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Due to his simple austere lifestyle and religious puritanism, Aurangzeb was known in history as 'Zinda Peir'."
    },
    {
        "question": "Which Mughal emperor introduced the religious syncretism known as 'Din-i-Ilahi'?\n\n[SSC GD 27-Jan-2023 Shift-4]",
        "options": ["Babur", "Humayun", "Akbar", "Shah Jahan"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Emperor Akbar formulated 'Din-i-Ilahi' in 1582 AD, blending ethical doctrines from various prominent religions."
    },
    {
        "question": "Who established the 'Ramakrishna Mission' in Kolkata in the year 1897?\n\n[SSC MTS 16-Jun-2023 Shift-2]",
        "options": ["Swami Vivekananda", "Ramakrishna Paramahamsa", "Swami Dayananda Saraswati", "Debendranath Tagore"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Swami Vivekananda founded the Ramakrishna Mission in memory of his spiritual guru, Ramakrishna Paramahamsa."
    },
    {
        "question": "In which year and under which Viceroy did the Partition of Bengal take place?\n\n[SSC GD 06-Feb-2023 Shift-1]",
        "options": ["1905, Lord Curzon", "1911, Lord Hardinge", "1905, Lord Minto", "1919, Lord Chelmsford"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Lord Curzon enforced the Partition of Bengal in 1905 under the pretext of administrative efficiency."
    },
    {
        "question": "During which movement did Mahatma Gandhi give the famous slogan 'Do or Die'?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["Non-Cooperation Movement", "Civil Disobedience Movement", "Quit India Movement", "Champaran Satyagraha"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Gandhiji raised the slogan 'Do or Die' during the historic Quit India Movement, launched on August 8, 1942, in Bombay."
    },
    {
        "question": "सिंधु घाटी सभ्यता का प्रमुख बंदरगाह शहर 'लोथल' वर्तमान में किस राज्य में स्थित है?\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["राजस्थान", "पंजाब", "गुजरात", "हरियाणा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 लोथल गुजरात के भाल क्षेत्र में भोगवा नदी के तट पर स्थित सिंधु घाटी सभ्यता का एक प्रमुख बंदरगाह था।"
    },
    {
        "question": "जैन धर्म के 24वें और अंतिम तीर्थंकर कौन थे?\n\n[SSC MTS 03-May-2023 Shift-1]",
        "options": ["ऋषभदेव", "पार्श्वनाथ", "महावीर स्वामी", "अरिष्टनेमि"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 वर्धमान महावीर जैन धर्म के 24वें तीर्थंकर थे। ऋषभदेव पहले और पार्श्वनाथ 23वें तीर्थंकर थे।"
    },
    {
        "question": "कौटिल्य (चाणक्य) द्वारा रचित प्रसिद्ध पुस्तक कौन सी है?\n\n[SSC CHSL 15-Mar-2023 Shift-3]",
        "options": ["इंडिका", "अर्थशास्त्र", "मुद्राराक्षस", "राजतरंगिणी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 चाणक्य द्वारा रचित 'अर्थशास्त्र' मौर्यकालीन राजनीति, लोक प्रशासन और अर्थशास्त्र पर आधारित एक प्रसिद्ध ग्रंथ है।"
    },
    {
        "question": "प्रसिद्ध चीनी यात्री 'ह्वेनसांग' (Hiuen Tsang) किस राजा के शासनकाल में भारत आया था?\n\n[SSC GD 17-Jan-2023 Shift-4]",
        "options": ["चंद्रगुप्त मौर्य", "चंद्रगुप्त द्वितीय", "हर्षवर्धन", "कनिष्क"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 चीनी बौद्ध भिक्षु ह्वेनसांग सम्राट हर्षवर्धन के शासनकाल में बौद्ध ग्रंथों का अध्ययन करने भारत आया था।"
    },
    {
        "question": "लाखबख्श (लाखों का दान देने वाला) की उपाधि दिल्ली सल्तनत के किस शासक को दी गई थी?\n\n[SSC MTS 10-May-2023 Shift-2]",
        "options": ["इल्तुतमिश", "कुतुबुद्दीन ऐबक", "बलबन", "अलाउद्दीन खिलजी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 अपनी अत्यधिक उदारता और दानशीलता के कारण कुतुबुद्दीन ऐबक को 'लाखबख्श' कहा जाता था।"
    },
    {
        "question": "पानीपत की पहली लड़ाई (1526) में बाबर ने किस सुल्तान को हराया था?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["बहलोल लोदी", "सिकंदर लोदी", "इब्राहिम लोदी", "राणा सांगा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 21 अप्रैल 1526 को पानीपत के प्रथम युद्ध में बाबर ने इब्राहिम लोदी को हराकर भारत में मुगल साम्राज्य की नींव रखी।"
    },
    {
        "question": "अकबरनामा (Akbarnama) पुस्तक के लेखक कौन हैं?\n\n[SSC GD 25-Jan-2023 Shift-1]",
        "options": ["बीरबल", "अब्दुल रहीम खान-ए-खाना", "फैजी", "अबुल फजल"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 अबुल फजल ने मुगल सम्राट अकबर के जीवन और शासनकाल पर आधारित 'अकबरनामा' की रचना की थी।"
    },
    {
        "question": "कोलकाता में 'ब्रह्म समाज' (Brahmo Samaj) की स्थापना 1828 में किसने की थी?\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["स्वामी विवेकानंद", "राजा राममोहन राय", "ईश्वर चंद्र विद्यासागर", "केशव चंद्र सेन"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 राजा राममोहन राय ने सामाजिक कुरीतियों जैसे सती प्रथा के विरोध के लिए 1828 में ब्रह्म समाज की स्थापना की थी।"
    },
    {
        "question": "1857 के महान विद्रोह की शुरुआत किस शहर की छावनी से हुई थी?\n\n[SSC GD 03-Feb-2023 Shift-2]",
        "options": ["झांसी", "मेरठ", "कानपुर", "बैरकपुर"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 10 मई 1857 को मेरठ की छावनी के भारतीय सैनिकों ने आधिकारिक तौर पर इस क्रांति की शुरुआत की थी।"
    },
    {
        "question": "महात्मा गांधी को सर्वप्रथम 'राष्ट्रपिता' कहकर किसने संबोधित किया था?\n\n[SSC CHSL 17-Mar-2023 Shift-4]",
        "options": ["जवाहरलाल नेहरू", "रवींद्रनाथ टैगोर", "सुभाष चंद्र बोस", "सरदार पटेल"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 1944 में सिंगापुर से रेडियो रंगून के माध्यम से सुभाष चंद्र बोस ने गांधी जी को सबसे पहले 'राष्ट्रपिता' संबोधित किया था।"
    },
    {
        "question": "In which present-day state is 'Lothal', the major port city of the Indus Valley Civilization, located?\n\n[SSC GD 11-Jan-2023 Shift-2]",
        "options": ["Rajasthan", "Punjab", "Gujarat", "Haryana"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Lothal was a major ancient port city of the Indus Valley Civilization located on the banks of the Bhogava river in Gujarat."
    },
    {
        "question": "Who was the 24th and last Tirthankara of Jainism?\n\n[SSC MTS 03-May-2023 Shift-1]",
        "options": ["Rishabhdev", "Parshvanath", "Mahavira Swami", "Arishtanemi"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Vardhamana Mahavira was the 24th Tirthankara of Jainism. Rishabhdev was the 1st and Parshvanath was the 23rd."
    },
    {
        "question": "Which famous book was authored by Kautilya (Chanakya)?\n\n[SSC CHSL 15-Mar-2023 Shift-3]",
        "options": ["Indica", "Arthashastra", "Mudrarakshasa", "Rajatarangini"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 'Arthashastra' is a famous book composed by Chanakya, focusing on statecraft, economic policy, and military strategy during the Mauryan era."
    },
    {
        "question": "The famous Chinese traveler 'Hiuen Tsang' visited India during the reign of which king?\n\n[SSC GD 17-Jan-2023 Shift-4]",
        "options": ["Chandragupta Maurya", "Chandragupta II", "Harshavardhana", "Kanishka"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Chinese Buddhist monk Hiuen Tsang traveled to India during the reign of King Harshavardhana to collect Buddhist texts."
    },
    {
        "question": "Which ruler of the Delhi Sultanate was given the title of 'Lakh Baksh' (Giver of Lakhs)?\n\n[SSC MTS 10-May-2023 Shift-2]",
        "options": ["Iltutmish", "Qutb-ud-din Aibak", "Balban", "Alauddin Khalji"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Due to his excessive generosity and charity, Qutb-ud-din Aibak was commonly referred to as 'Lakh Baksh'."
    },
    {
        "question": "Which sultan was defeated by Babur in the First Battle of Panipat (1526)?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["Bahlul Lodi", "Sikandar Lodi", "Ibrahim Lodi", "Rana Sanga"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 On April 21, 1526, Babur defeated Ibrahim Lodi in the First Battle of Panipat, establishing the Mughal Empire in India."
    },
    {
        "question": "Who is the author of the book 'Akbarnama'?\n\n[SSC GD 25-Jan-2023 Shift-1]",
        "options": ["Birbal", "Abdul Rahim Khan-i-Khanan", "Faizi", "Abul Fazl"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Abul Fazl wrote the 'Akbarnama', which provides an official and detailed history of the life and reign of Mughal Emperor Akbar."
    },
    {
        "question": "Who founded the 'Brahmo Samaj' in Kolkata in the year 1828?\n\n[SSC MTS 19-May-2023 Shift-2]",
        "options": ["Swami Vivekananda", "Raja Ram Mohan Roy", "Ishwar Chandra Vidyasagar", "Keshub Chandra Sen"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Raja Ram Mohan Roy established the Brahmo Samaj in 1828 to fight social evils like the Sati system."
    },
    {
        "question": "From which city's military cantonment did the great revolt of 1857 officially begin?\n\n[SSC GD 03-Feb-2023 Shift-2]",
        "options": ["Jhansi", "Meerut", "Kanpur", "Barrackpore"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The uprising officially started on May 10, 1857, when Indian sepoys mutinied in the military cantonment at Meerut."
    },
    {
        "question": "Who was the first to address Mahatma Gandhi as the 'Father of the Nation'?\n\n[SSC CHSL 17-Mar-2023 Shift-4]",
        "options": ["Jawaharlal Nehru", "Rabindranath Tagore", "Subhas Chandra Bose", "Sardar Patel"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 In 1944, Subhas Chandra Bose addressed Gandhiji as the 'Father of the Nation' for the first time during a radio broadcast from Singapore."
    },
    {
        "question": "सिंधु घाटी सभ्यता का कौन सा स्थल 'मृतकों का टीला' (Mound of the Dead) कहलाता है?\n\n[SSC GD 10-Jan-2023 Shift-2]",
        "options": ["हड़प्पा", "लोथल", "कालीबंगा", "मोहनजोदड़ो"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 सिन्धी भाषा में मोहनजोदड़ो का शाब्दिक अर्थ 'मृतकों का टीला' होता है।"
    },
    {
        "question": "गौतम बुद्ध ने अपना पहला उपदेश कहाँ दिया था, जिसे 'धर्मचक्रप्रवर्तन' कहा जाता है?\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["लुम्बिनी", "बोधगया", "सारनाथ", "कुशीनगर"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 ज्ञान प्राप्ति के बाद महात्मा बुद्ध ने अपना प्रथम उपदेश सारनाथ (ऋषिपत्तनम) में दिया था।"
    },
    {
        "question": "प्रसिद्ध सम्राट अशोक किस राजवंश से संबंधित थे?\n\n[SSC CHSL 14-Mar-2023 Shift-1]",
        "options": ["गुप्त वंश", "मौर्य वंश", "हर्यक वंश", "शुंग वंश"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 सम्राट अशोक मौर्य वंश के तीसरे शासक थे, जो बिंदुसार के पुत्र और चंद्रगुप्त मौर्य के पौत्र थे।"
    },
    {
        "question": "भारत का नेपोलियन (Napoleon of India) किसे कहा जाता है?\n\n[SSC GD 16-Jan-2023 Shift-3]",
        "options": ["चंद्रगुप्त प्रथम", "समुद्रगुप्त", "स्कंदगुप्त", "अशोक"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 इतिहासकार वी.ए. स्मिथ ने समुद्रगुप्त की सैन्य विजयों के कारण उसे 'भारत का नेपोलियन' कहा था।"
    },
    {
        "question": "दिल्ली सल्तनत की पहली और एकमात्र महिला शासिका कौन थी?\n\n[SSC MTS 08-May-2023 Shift-2]",
        "options": ["रजिया सुल्तान", "चाँद बीबी", "नूरजहाँ", "मुमताज महल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 रजिया सुल्तान इल्तुतमिश की पुत्री थी, जिसने 1236 से 1240 ई. तक दिल्ली पर शासन किया।"
    },
    {
        "question": "विजयनगर साम्राज्य की स्थापना 1336 ई. में किन दो भाइयों ने की थी?\n\n[SSC CHSL 11-Aug-2023 Shift-4]",
        "options": ["कृष्णदेव राय और अच्युत राय", "हरिहर और बुक्का", "देवराय प्रथम और द्वितीय", "सदाशिव और रामराय"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 मोहम्मद बिन तुगलक के काल में हरिहर और बुक्का नाम के दो भाइयों ने तुंगभद्रा नदी के तट पर विजयनगर की स्थापना की थी।"
    },
    {
        "question": "आर्य समाज (Arya Samaj) की स्थापना 1875 में किसने की थी?\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["राजा राममोहन राय", "स्वामी विवेकानंद", "स्वामी दयानंद सरस्वती", "आत्माराम पांडुरंग"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 स्वामी दयानंद सरस्वती ने मुंबई में आर्य समाज की स्थापना की और 'वेदों की ओर लौटो' का नारा दिया।"
    },
    {
        "question": "भारतीय राष्ट्रीय कांग्रेस (INC) की स्थापना किस वर्ष हुई थी?\n\n[SSC MTS 15-Jun-2023 Shift-1]",
        "options": ["1882", "1885", "1890", "1905"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 28 दिसंबर 1885 को बम्बई में ए.ओ. ह्यूम (A.O. Hume) के प्रयासों से कांग्रेस की स्थापना की गई थी।"
    },
    {
        "question": "जलियांवाला बाग हत्याकांड किस वर्ष और किस तारीख को हुआ था?\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["13 अप्रैल 1919", "15 अगस्त 1919", "26 जनवरी 1920", "10 मार्च 1919"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 पंजाब के अमृतसर में स्थित जलियांवाला बाग में बैसाखी के दिन 13 अप्रैल 1919 को जनरल डायर ने अंधाधुंध गोलियां चलवाई थीं।"
    },
    {
        "question": "गांधी जी ने भारत में अपना पहला सफल सत्याग्रह कहाँ शुरू किया था?\n\n[SSC CHSL 17-Mar-2023 Shift-2]",
        "options": ["खेड़ा", "अहमदाबाद", "चंपारण", "बारदोली"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 बिहार के चंपारण में 1917 में नील की खेती (तिनकठिया पद्धति) के विरोध में गांधी जी का भारत में पहला सत्याग्रह हुआ था।"
    },
    {
        "question": "Which site of the Indus Valley Civilization is known as the 'Mound of the Dead'?\n\n[SSC GD 10-Jan-2023 Shift-2]",
        "options": ["Harappa", "Lothal", "Kalibangan", "Mohenjo-daro"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 In the Sindhi language, the literal meaning of Mohenjo-daro is 'Mound of the Dead'."
    },
    {
        "question": "Where did Gautam Buddha deliver his first sermon, which is known as 'Dhammacakkappavattana'?\n\n[SSC MTS 02-May-2023 Shift-1]",
        "options": ["Lumbini", "Bodh Gaya", "Sarnath", "Kushinagar"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 After attaining enlightenment, Mahatma Buddha delivered his first sermon at Sarnath (Rishipatana)."
    },
    {
        "question": "The famous Emperor Ashoka belonged to which dynasty?\n\n[SSC CHSL 14-Mar-2023 Shift-1]",
        "options": ["Gupta Dynasty", "Maurya Dynasty", "Haryanka Dynasty", "Shunga Dynasty"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Emperor Ashoka was the third ruler of the Maurya dynasty, son of Bindusara and grandson of Chandragupta Maurya."
    },
    {
        "question": "Who is popularly known as the 'Napoleon of India'?\n\n[SSC GD 16-Jan-2023 Shift-3]",
        "options": ["Chandragupta I", "Samudragupta", "Skandagupta", "Ashoka"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Historian V.A. Smith called Samudragupta the 'Napoleon of India' due to his vast military conquests."
    },
    {
        "question": "Who was the first and only woman ruler of the Delhi Sultanate?\n\n[SSC MTS 08-May-2023 Shift-2]",
        "options": ["Razia Sultan", "Chand Bibi", "Noor Jahan", "Mumtaz Mahal"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Razia Sultan was the daughter of Iltutmish, who ruled Delhi from 1236 to 1240 AD."
    },
    {
        "question": "Who founded the Vijayanagara Empire in 1336 AD?\n\n[SSC CHSL 11-Aug-2023 Shift-4]",
        "options": ["Krishnadevaraya and Achyuta Raya", "Harihara and Bukka", "Devaraya I and II", "Sadashiva and Ramaraya"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 During the reign of Muhammad bin Tughluq, two brothers named Harihara and Bukka founded Vijayanagara on the banks of the Tungabhadra river."
    },
    {
        "question": "Who founded the Arya Samaj in the year 1875?\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["Raja Ram Mohan Roy", "Swami Vivekananda", "Swami Dayananda Saraswati", "Atmaram Pandurang"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Swami Dayananda Saraswati established the Arya Samaj in Mumbai and gave the famous slogan 'Back to the Vedas'."
    },
    {
        "question": "In which year was the Indian National Congress (INC) established?\n\n[SSC MTS 15-Jun-2023 Shift-1]",
        "options": ["1882", "1885", "1890", "1905"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Congress was founded on December 28, 1885, in Bombay through the efforts of A.O. Hume."
    },
    {
        "question": "On which date did the infamous Jallianwala Bagh Massacre take place?\n\n[SSC GD 02-Feb-2023 Shift-3]",
        "options": ["13 April 1919", "15 August 1919", "26 January 1920", "10 March 1919"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 On the day of Baisakhi, 13 April 1919, General Dyer ordered indiscriminate firing on an unarmed crowd at Jallianwala Bagh in Amritsar, Punjab."
    },
    {
        "question": "Where did Mahatma Gandhi start his first successful Satyagraha in India?\n\n[SSC CHSL 17-Mar-2023 Shift-2]",
        "options": ["Kheda", "Ahmedabad", "Champaran", "Bardoli"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Gandhiji's first Satyagraha in India took place at Champaran (Bihar) in 1917, protesting against the Tinkathia system of indigo farming."
    },
    {
        "question": "कावेरी नदी का उद्गम स्थल (Origin) किस राज्य में है?\n\n[SSC GD 12-Jan-2023 Shift-4]",
        "options": ["केरल", "तमिलनाडु", "कर्नाटक", "आंध्र प्रदेश"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 कावेरी नदी कर्नाटक के कोडागु जिले में ब्रह्मगिरि पहाड़ियों से निकलती है।"
    },
    {
        "question": "वायुमंडल में सबसे अधिक मात्रा में पाई जाने वाली गैस कौन सी है?\n\n[SSC MTS 04-May-2023 Shift-3]",
        "options": ["ऑक्सीजन", "नाइट्रोजन", "कार्बन डाइऑक्साइड", "आर्गन"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 हमारे वायुमंडल में सबसे अधिक मात्रा में नाइट्रोजन गैस (लगभग 78%) पाई जाती है।"
    },
    {
        "question": "केवलादेव राष्ट्रीय उद्यान (Keoladeo National Park) किस राज्य में है?\n\n[SSC CHSL 14-Mar-2023 Shift-1]",
        "options": ["मध्य प्रदेश", "गुजरात", "हरियाणा", "राजस्थान"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 केवलादेव राष्ट्रीय उद्यान (जिसे भरतपुर पक्षी अभयारण्य भी कहते हैं) राजस्थान में स्थित है।"
    },
    {
        "question": "क्षेत्रफल के हिसाब से भारत का सबसे बड़ा राज्य कौन सा है?\n\n[SSC GD 17-Jan-2023 Shift-3]",
        "options": ["मध्य प्रदेश", "उत्तर Pradesh", "राजस्थान", "महाराष्ट्र"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 क्षेत्रफल में राजस्थान भारत का सबसे बड़ा राज्य है और गोवा सबसे छोटा है।"
    },
    {
        "question": "भारत का सबसे ऊँचा बांध 'टिहरी बांध' किस राज्य में स्थित है?\n\n[SSC MTS 11-May-2023 Shift-2]",
        "options": ["हिमाचल प्रदेश", "उत्तराखंड", "जम्मू-कश्मीर", "अरुणाचल प्रदेश"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 टिहरी बांध उत्तराखंड में भागीरथी नदी पर बना है, जो भारत का सबसे ऊँचा बांध है।"
    },
    {
        "question": "भारत का सबसे बड़ा चावल उत्पादक राज्य कौन सा है?\n\n[SSC CHSL 16-Mar-2023 Shift-2]",
        "options": ["उत्तर प्रदेश", "पंजाब", "आंध्र प्रदेश", "पश्चिम बंगाल"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 पश्चिम बंगाल भारत में सबसे अधिक चावल उत्पादन करने वाला राज्य है।"
    },
    {
        "question": "नर्मदा नदी अमरकंटक से निकलकर किस खाड़ी या सागर में गिरती है?\n\n[SSC GD 27-Jan-2023 Shift-3]",
        "options": ["बंगाल की खाड़ी", "खंभात की खाड़ी", "मन्नार की खाड़ी", "कच्छ की खाड़ी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 नर्मदा नदी पश्चिम की ओर बहती है और गुजरात के पास अरब सागर की खंभात की खाड़ी में गिरती है।"
    },
    {
        "question": "कोलार (Kolar) सोने की खदानें भारत के किस राज्य में स्थित हैं?\n\n[SSC MTS 16-Jun-2023 Shift-1]",
        "options": ["आंध्र प्रदेश", "कर्नाटक", "तमिलनाडु", "केरल"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 कोलार गोल्ड फील्ड्स (KGF) कर्नाटक राज्य में स्थित प्रसिद्ध सोने की खदानें हैं।"
    },
    {
        "question": "भारत और पाकिस्तान के बीच की सीमा रेखा को क्या कहा जाता है?\n\n[SSC GD 06-Feb-2023 Shift-2]",
        "options": ["मैकमोहन रेखा", "डूरंड रेखा", "रेडक्लिफ रेखा", "हिंडनबर्ग रेखा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भारत और पाकिस्तान के बीच की अंतरराष्ट्रीय सीमा को रेडक्लिफ रेखा (Radcliffe Line) कहते हैं।"
    },
    {
        "question": "काजीरंगा राष्ट्रीय उद्यान भारत के किस राज्य में स्थित है?\n\n[SSC CHSL 17-Mar-2023 Shift-3]",
        "options": ["असम", "मेघालय", "त्रिपुरा", "मिजोरम"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 काजीरंगा राष्ट्रीय उद्यान असम में स्थित है, जो एक सींग वाले गैंडे के लिए प्रसिद्ध है।"
    },
    {
        "question": "In which state is the origin of the Cauvery River located?\n\n[SSC GD 12-Jan-2023 Shift-4]",
        "options": ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Cauvery River originates from the Brahmagiri hills in the Kodagu district of Karnataka."
    },
    {
        "question": "Which gas is found in the highest abundance in the Earth's atmosphere?\n\n[SSC MTS 04-May-2023 Shift-3]",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Nitrogen is the most abundant gas in our atmosphere, making up about 78% of total volume."
    },
    {
        "question": "In which state is the Keoladeo National Park located?\n\n[SSC CHSL 14-Mar-2023 Shift-1]",
        "options": ["Madhya Pradesh", "Gujarat", "Haryana", "Rajasthan"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Keoladeo National Park (formerly known as Bharatpur Bird Sanctuary) is located in Rajasthan."
    },
    {
        "question": "Which is the largest state of India in terms of area?\n\n[SSC GD 17-Jan-2023 Shift-3]",
        "options": ["Madhya Pradesh", "Uttar Pradesh", "Rajasthan", "Maharashtra"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Rajasthan is the largest state in India by area, while Goa is the smallest."
    },
    {
        "question": "In which state is 'Tehri Dam', the highest dam in India, located?\n\n[SSC MTS 11-May-2023 Shift-2]",
        "options": ["Himachal Pradesh", "Uttarakhand", "Jammu and Kashmir", "Arunachal Pradesh"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Tehri Dam is built on the Bhagirathi river in Uttarakhand and is the highest dam in India."
    },
    {
        "question": "Which is the largest rice-producing state in India?\n\n[SSC CHSL 16-Mar-2023 Shift-2]",
        "options": ["Uttar Pradesh", "Punjab", "Andhra Pradesh", "West Bengal"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 West Bengal is the highest rice-producing state in India."
    },
    {
        "question": "The Narmada River originates from Amarkantak and empties into which gulf or sea?\n\n[SSC GD 27-Jan-2023 Shift-3]",
        "options": ["Bay of Bengal", "Gulf of Khambhat", "Gulf of Mannar", "Gulf of Kutch"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The westward-flowing Narmada river drains into the Gulf of Khambhat in the Arabian Sea near Gujarat."
    },
    {
        "question": "In which Indian state are the Kolar gold mines located?\n\n[SSC MTS 16-Jun-2023 Shift-1]",
        "options": ["Andhra Pradesh", "Karnataka", "Tamil Nadu", "Kerala"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Kolar Gold Fields (KGF) are famous gold mines located in the state of Karnataka."
    },
    {
        "question": "What is the boundary line between India and Pakistan called?\n\n[SSC GD 06-Feb-2023 Shift-2]",
        "options": ["McMahon Line", "Durand Line", "Radcliffe Line", "Hindenburg Line"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The international boundary line between India and Pakistan is called the Radcliffe Line."
    },
    {
        "question": "In which state of India is the Kaziranga National Park located?\n\n[SSC CHSL 17-Mar-2023 Shift-3]",
        "options": ["Assam", "Meghalaya", "Tripura", "Mizoram"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Kaziranga National Park is located in Assam and is world-famous for its one-horned rhinoceros population."
    },
    {
        "question": "सिमलीपाल राष्ट्रीय उद्यान (Simlipal National Park) भारत के किस राज्य में स्थित है?\n\n[SSC GD 11-Jan-2023 Shift-4]",
        "options": ["ओडिशा", "झारखंड", "छत्तीसगढ़", "पश्चिम बंगाल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 सिमलीपाल राष्ट्रीय उद्यान और मयूरभंज हाथी अभयारण्य ओडिशा राज्य में स्थित हैं।"
    },
    {
        "question": "ओजोन परत (Ozone Layer) वायुमंडल की किस परत में पाई जाती है?\n\n[SSC MTS 03-May-2023 Shift-2]",
        "options": ["क्षोभमण्डल", "समतापमण्डल", "मध्यमण्डल", "बाह्यमण्डल"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 ओजोन परत समतापमण्डल (Stratosphere) में स्थित है, जो सूर्य की हानिकारक पराबैंगनी किरणों को सोखती है।"
    },
    {
        "question": "भारत में श्वेत क्रांति (White Revolution) का जनक किसे कहा जाता है?\n\n[SSC CHSL 15-Mar-2023 Shift-1]",
        "options": ["एम.एस. स्वामीनाथन", "वर्गिज कुरियन", "नॉर्मन बोरलॉग", "सैम पित्रोदा"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 भारत में डॉ. वर्गिज कुरियन को श्वेत क्रांति (दूध उत्पादन) और 'ऑपरेशन फ्लड' का जनक माना जाता है।"
    },
    {
        "question": "भारत की किस नदी को 'नमक की नदी' (Salt River) कहा जाता है?\n\n[SSC GD 17-Jan-2023 Shift-2]",
        "options": ["साबरमती", "लूनी नदी", "माही नदी", "तापी नदी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 राजस्थान के थार मरुस्थल से बहने वाली लूनी नदी को लवणीय जल के कारण 'नमक की नदी' भी कहते हैं।"
    },
    {
        "question": "कपिली (Kapili) निम्नलिखित में से किस नदी की एक प्रमुख सहायक नदी है?\n\n[SSC MTS 10-May-2023 Shift-1]",
        "options": ["गंगा", "ब्रह्मपुत्र", "सिंधु", "गोदावरी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 कपिली नदी पूर्वोत्तर भारत में ब्रह्मपुत्र नदी की एक प्रमुख दक्षिण-तट सहायक नदी है।"
    },
    {
        "question": "भारत का सबसे बड़ा बॉक्साइट उत्पादक राज्य कौन सा है?\n\n[SSC CHSL 14-Mar-2023 Shift-4]",
        "options": ["ओडिशा", "झारखंड", "गुजरात", "महाराष्ट्र"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 भारत में आधे से अधिक बॉक्साइट (एल्युमिनियम का अयस्क) का उत्पादन अकेले ओडिशा राज्य में होता है।"
    },
    {
        "question": "राणा प्रताप सागर बांध किस नदी पर निर्मित है?\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["नर्मदा नदी", "चम्बल नदी", "सोन नदी", "बेतवा नदी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 राजस्थान में स्थित राणा प्रताप सागर बांध चम्बल नदी पर बनाई गई प्रमुख जलविद्युत परियोजनाओं में से एक है।"
    },
    {
        "question": "गिर राष्ट्रीय उद्यान (Gir National Park) किसके संरक्षण के लिए प्रसिद्ध है?\n\n[SSC MTS 19-May-2023 Shift-3]",
        "options": ["एशियाई शेर", "रॉयल बंगाल टाइगर", "एक सींग वाला गैंडा", "हाथी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 गुजरात में स्थित गिर राष्ट्रीय उद्यान विशुद्ध रूप से 'एशियाई शेरों' (Asiatic Lions) के लिए जाना जाता है।"
    },
    {
        "question": "भारत का सुदूर दक्षिणी बिंदु (Southernmost Point) कौन सा है?\n\n[SSC GD 03-Feb-2023 Shift-4]",
        "options": ["इंदिरा कॉल", "केप कमोरिन", "इंदिरा पॉइंट", "किबिथू"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भारत का सबसे दक्षिणी बिंदु 'इंदिरा पॉइंट' अंडमान और निकोबार के ग्रेट निकोबार द्वीप पर स्थित है।"
    },
    {
        "question": "भूमध्य रेखा के सबसे निकट स्थित भारतीय स्थान कौन सा है?\n\n[SSC CHSL 17-Mar-2023 Shift-2]",
        "options": ["कन्याकुमारी", "रामेश्वरम", "इंदिरा पॉइंट", "मिनिकॉय द्वीप"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 अंडमान और निकोबार में स्थित 'इंदिरा पॉइंट' भूमध्य रेखा (Equator) के सबसे नजदीक का भारतीय क्षेत्र है।"
    },
    {
        "question": "In which Indian state is the Simlipal National Park located?\n\n[SSC GD 11-Jan-2023 Shift-4]",
        "options": ["Odisha", "Jharkhand", "Chhattisgarh", "West Bengal"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Simlipal National Park and Mayurbhanj Elephant Reserve are located in the state of Odisha."
    },
    {
        "question": "In which layer of the atmosphere is the Ozone Layer found?\n\n[SSC MTS 03-May-2023 Shift-2]",
        "options": ["Troposphere", "Stratosphere", "Mesosphere", "Exosphere"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The ozone layer is located in the Stratosphere, which absorbs harmful ultraviolet (UV) radiation from the sun."
    },
    {
        "question": "Who is known as the father of the 'White Revolution' in India?\n\n[SSC CHSL 15-Mar-2023 Shift-1]",
        "options": ["M.S. Swaminathan", "Verghese Kurien", "Norman Borlaug", "Sam Pitroda"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Dr. Verghese Kurien is considered the father of the White Revolution (milk production) and 'Operation Flood' in India."
    },
    {
        "question": "Which river in India is also referred to as the 'Salt River'?\n\n[SSC GD 17-Jan-2023 Shift-2]",
        "options": ["Sabarmati", "Luni River", "Mahi River", "Tapi River"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Luni River flowing through the Thar Desert of Rajasthan is called the Salt River due to its brackish water."
    },
    {
        "question": "Kapili is a major tributary of which of the following rivers?\n\n[SSC MTS 10-May-2023 Shift-1]",
        "options": ["Ganga", "Brahmaputra", "Indus", "Godavari"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Kapili River is a major south-bank tributary of the Brahmaputra River in Northeast India."
    },
    {
        "question": "Which is the largest bauxite-producing state in India?\n\n[SSC CHSL 14-Mar-2023 Shift-4]",
        "options": ["Odisha", "Jharkhand", "Gujarat", "Maharashtra"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Odisha is the leading bauxite producer in India, accounting for more than half of the country's total output."
    },
    {
        "question": "On which river is the Rana Pratap Sagar Dam constructed?\n\n[SSC GD 24-Jan-2023 Shift-2]",
        "options": ["Narmada River", "Chambal River", "Sone River", "Betwa River"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Rana Pratap Sagar Dam in Rajasthan is built on the Chambal River as a key hydroelectric project."
    },
    {
        "question": "The Gir National Park is famous for the protection of which animal?\n\n[SSC MTS 19-May-2023 Shift-3]",
        "options": ["Asiatic Lion", "Royal Bengal Tiger", "One-horned Rhinoceros", "Elephant"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Located in Gujarat, the Gir National Park is world-renowned exclusively for protecting Asiatic Lions."
    },
    {
        "question": "Which is the southernmost point of Indian territory?\n\n[SSC GD 03-Feb-2023 Shift-4]",
        "options": ["Indira Col", "Cape Comorin", "Indira Point", "Kirbithu"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The southernmost point of India is 'Indira Point', located on Great Nicobar Island in the Andaman and Nicobar archipelago."
    },
    {
        "question": "Which Indian location is situated closest to the Equator?\n\n[SSC CHSL 17-Mar-2023 Shift-2]",
        "options": ["Kanyakumari", "Rameshwaram", "Indira Point", "Minicoy Island"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 'Indira Point' in the Andaman and Nicobar Islands is geographically the closest Indian territory to the Equator."
    },
    {
        "question": "भारत का एकमात्र तैरता हुआ राष्ट्रीय उद्यान 'केबुल लामजाओ' कहाँ स्थित है?\n\n[SSC GD 12-Jan-2023 Shift-1]",
        "options": ["असम", "मणिपुर", "मेघालय", "त्रिपुरा"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 मणिपुर की लोकटक झील पर स्थित केबुल लामजाओ (Keibul Lamjao) विश्व का एकमात्र तैरता हुआ राष्ट्रीय उद्यान है।"
    },
    {
        "question": "वायुमंडल की सबसे निचली परत को क्या कहा जाता है?\n\n[SSC MTS 02-May-2023 Shift-3]",
        "options": ["समतापमण्डल", "ओजोनमण्डल", "क्षोभमण्डल", "आयन्मण्डल"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 क्षोभमण्डल (Troposphere) वायुमंडल की सबसे निचली परत है, जहाँ मौसम की सभी घटनाएँ घटित होती हैं।"
    },
    {
        "question": "गुलाबी नगरी (Pink City) के नाम से किसे जाना जाता है?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["जोधपुर", "उदयपुर", "जयपुर", "जैसलमेर"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 राजस्थान की राजधानी जयपुर को अपनी अनूठी वास्तुकला और गुलाबी पत्थरों के कारण 'गुलाबी नगरी' कहा जाता है।"
    },
    {
        "question": "दक्षिण भारत की सबसे लंबी नदी कौन सी है?\n\n[SSC GD 17-Jan-2023 Shift-3]",
        "options": ["कृष्णा", "कावेरी", "गोदावरी", "महानदी"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 गोदावरी नदी प्रायद्वीपीय या दक्षिण भारत की सबसे लंबी नदी (1465 किमी) है।"
    },
    {
        "question": "भारत में सबसे अधिक चाय उत्पादक राज्य कौन सा है?\n\n[SSC MTS 09-May-2023 Shift-1]",
        "options": ["पश्चिम बंगाल", "असम", "केरल", "तमिलनाडु"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 असम भारत का सबसे बड़ा चाय उत्पादक राज्य है, जबकि दार्जिलिंग (पश्चिम बंगाल) की चाय अपनी सुगंध के लिए प्रसिद्ध है।"
    },
    {
        "question": "चिल्का झील किस राज्य में स्थित है?\n\n[SSC CHSL 16-Mar-2023 Shift-4]",
        "options": ["ओडिशा", "आंध्र प्रदेश", "तमिलनाडु", "केरल"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 ओडिशा में स्थित चिल्का झील भारत की सबसे बड़ी तटीय लैगून झील और खारे पानी की झील है।"
    },
    {
        "question": "काली मिट्टी का दूसरा नाम क्या है?\n\n[SSC GD 25-Jan-2023 Shift-4]",
        "options": ["बांगर मिट्टी", "खादर मिट्टी", "रेगुर मिट्टी", "लेटराइट मिट्टी"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 काली मिट्टी को 'रेगुर मिट्टी' भी कहा जाता है, जो कपास की खेती के लिए सर्वोत्तम होती है।"
    },
    {
        "question": "शिवसमुद्रम जलप्रपात किस नदी पर स्थित है?\n\n[SSC MTS 15-Jun-2023 Shift-2]",
        "options": ["नर्मदा नदी", "कृष्णा नदी", "गोदावरी नदी", "कावेरी नदी"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 शिवसमुद्रम जलप्रपात कर्नाटक में कावेरी नदी पर स्थित एक प्रसिद्ध जलप्रपात है।"
    },
    {
        "question": "भारत का सबसे बड़ा मरुस्थल कौन सा है?\n\n[SSC GD 06-Feb-2023 Shift-3]",
        "options": ["सहारा", "गोबी", "थार", "अटाकामा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 थार मरुस्थल (Thar Desert) भारत का सबसे बड़ा मरुस्थल है, जो मुख्य रूप से राजस्थान में फैला है।"
    },
    {
        "question": "दूधवा राष्ट्रीय उद्यान (Dudhwa National Park) कहाँ स्थित है?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["मध्य प्रदेश", "उत्तर प्रदेश", "बिहार", "उत्तराखंड"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 दूधवा राष्ट्रीय उद्यान उत्तर प्रदेश के लखीमपुर खीरी जिले में स्थित एक प्रसिद्ध बाघ अभयारण्य है।"
    },
    {
        "question": "Where is India's only floating national park 'Keibul Lamjao' located?\n\n[SSC GD 12-Jan-2023 Shift-1]",
        "options": ["Assam", "Manipur", "Meghalaya", "Tripura"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Keibul Lamjao, located on Loktak Lake in Manipur, is the only floating national park in the world."
    },
    {
        "question": "What is the lowest layer of the atmosphere called?\n\n[SSC MTS 02-May-2023 Shift-3]",
        "options": ["Stratosphere", "Ozonosphere", "Troposphere", "Ionosphere"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Troposphere is the lowest layer of the atmosphere, where all weather phenomena occur."
    },
    {
        "question": "Which city is known as the 'Pink City'?\n\n[SSC CHSL 14-Mar-2023 Shift-2]",
        "options": ["Jodhpur", "Udaipur", "Jaipur", "Jaisalmer"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Jaipur, the capital of Rajasthan, is known as the Pink City due to its unique architecture and pink-colored stones."
    },
    {
        "question": "Which is the longest river in South India?\n\n[SSC GD 17-Jan-2023 Shift-3]",
        "options": ["Krishna", "Cauvery", "Godavari", "Mahanadi"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Godavari river is the longest river in peninsular or South India (1465 km)."
    },
    {
        "question": "Which state is the largest producer of tea in India?\n\n[SSC MTS 09-May-2023 Shift-1]",
        "options": ["West Bengal", "Assam", "Kerala", "Tamil Nadu"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Assam is the largest tea-producing state in India, while Darjeeling (West Bengal) tea is famous for its unique aroma."
    },
    {
        "question": "In which state is Chilika Lake located?\n\n[SSC CHSL 16-Mar-2023 Shift-4]",
        "options": ["Odisha", "Andhra Pradesh", "Tamil Nadu", "Kerala"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 Chilika Lake in Odisha is the largest coastal lagoon lake and brackish saltwater lake in India."
    },
    {
        "question": "What is the alternative name for Black Soil?\n\n[SSC GD 25-Jan-2023 Shift-4]",
        "options": ["Bangar Soil", "Khadar Soil", "Regur Soil", "Laterite Soil"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Black soil is also known as 'Regur Soil' and is highly suitable for growing cotton crops."
    },
    {
        "question": "On which river is the Shivanasamudra Falls located?\n\n[SSC MTS 15-Jun-2023 Shift-2]",
        "options": ["Narmada River", "Krishna River", "Godavari River", "Cauvery River"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 Shivanasamudra Falls is a famous waterfall located on the Cauvery river in Karnataka."
    },
    {
        "question": "Which is the largest desert in India?\n\n[SSC GD 06-Feb-2023 Shift-3]",
        "options": ["Sahara", "Gobi", "Thar", "Atacama"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 The Thar Desert is the largest desert in India, spread primarily across Rajasthan."
    },
    {
        "question": "Where is the Dudhwa National Park located?\n\n[SSC CHSL 17-Mar-2023 Shift-1]",
        "options": ["Madhya Pradesh", "Uttar Pradesh", "Bihar", "Uttarakhand"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Dudhwa National Park is a renowned tiger reserve located in the Lakhimpur Kheri district of Uttar Pradesh."
    },
    {
        "question": "भारत में 'हरित क्रांति' (Green Revolution) का जनक किसे माना जाता है?\n\n[SSC GD 11-Jan-2023 Shift-1]",
        "options": ["वर्गिज कुरियन", "एम.एस. स्वामीनाथन", "सैम पित्रोदा", "नॉर्मन बोरलॉग"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 भारत में एम.एस. स्वामीनाथन को हरित क्रांति का जनक माना जाता है, जबकि विश्व में नॉर्मन बोरलॉग को इसका जनक माना जाता है।"
    },
    {
        "question": "लोनार झील (Lonar Lake) भारत के किस राज्य में स्थित है?\n\n[SSC MTS 05-May-2023 Shift-3]",
        "options": ["गुजरात", "राजस्थान", "महाराष्ट्र", "ओडिशा"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 महाराष्ट्र के बुलढाणा जिले में स्थित लोनार झील एक क्रेटर झील है, जिसका निर्माण उल्कापिंड के गिरने से हुआ था।"
    },
    {
        "question": "भारत का सबसे बड़ा कोयला उत्पादक राज्य कौन सा है?\n\n[SSC CHSL 15-Mar-2023 Shift-4]",
        "options": ["झारखंड", "छत्तीसगढ़", "ओडिशा", "पश्चिम बंगाल"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 कोयला उत्पादन (Production) के मामले में छत्तीसगढ़ प्रमुख राज्यों में है, जबकि कोयला भंडार (Reserves) सबसे ज्यादा झारखंड में हैं।"
    },
    {
        "question": "सरिस्का राष्ट्रीय उद्यान (Sariska National Park) कहाँ स्थित है?\n\n[SSC GD 17-Jan-2023 Shift-1]",
        "options": ["मध्य प्रदेश", "उत्तर प्रदेश", "गुजरात", "राजस्थान"],
        "correct_id": 3,
        "lang": "hindi",
        "explanation": "💡 सरिस्का बाघ अभयारण्य (Sariska Tiger Reserve) राजस्थान के अलवर जिले में स्थित है।"
    },
    {
        "question": "धुआंधार जलप्रपात (Dhuandhar Falls) किस नदी पर स्थित है?\n\n[SSC MTS 11-May-2023 Shift-1]",
        "options": ["नर्मदा नदी", "तापी नदी", "गोदावरी नदी", "महानदी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 धुआंधार जलप्रपात मध्य प्रदेश के जबलपुर में नर्मदा नदी पर स्थित एक प्रसिद्ध प्रपात है।"
    },
    {
        "question": "विश्व का सबसे बड़ा मरुस्थल कौन सा है?\n\n[SSC CHSL 13-Mar-2023 Shift-2]",
        "options": ["थार", "सहारा", "गोबी", "कालाहारी"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 अफ्रीका महाद्वीप में स्थित सहारा मरुस्थल विश्व का सबसे बड़ा गर्म मरुस्थल है।"
    },
    {
        "question": "टिहरी बांध (Tehri Dam) किस नदी पर बनाया गया है?\n\n[SSC GD 24-Jan-2023 Shift-4]",
        "options": ["अलकनंदा", "भागीरथी", "मंदाकिनी", "यमुना"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 उत्तराखंड में भागीरथी नदी पर बना टिहरी बांध भारत का सबसे ऊँचा बांध है।"
    },
    {
        "question": "भारत में सबसे पहले सूर्योदय किस राज्य में होता है?\n\n[SSC MTS 19-May-2023 Shift-1]",
        "options": ["असम", "नागालैंड", "अरुणाचल प्रदेश", "मणिपुर"],
        "correct_id": 2,
        "lang": "hindi",
        "explanation": "💡 भारत के सबसे पूर्वी छोर पर स्थित होने के कारण अरुणाचल प्रदेश में सबसे पहले सूर्योदय होता है।"
    },
    {
        "question": "चिल्का वन्यजीव अभयारण्य भारत के किस राज्य में स्थित है?\n\n[SSC GD 03-Feb-2023 Shift-1]",
        "options": ["पश्चिम बंगाल", "ओडिशा", "आंध्र प्रदेश", "तमिलनाडु"],
        "correct_id": 1,
        "lang": "hindi",
        "explanation": "💡 चिल्का झील और उससे जुड़ा अभयारण्य ओडिशा राज्य में स्थित है, जो प्रवासी पक्षियों के लिए प्रसिद्ध है।"
    },
    {
        "question": "एशिया की सबसे लंबी नदी कौन सी है?\n\n[SSC CHSL 17-Mar-2023 Shift-3]",
        "options": ["यांग्त्सी नदी", "गंगा नदी", "सिंधु नदी", "मेकांग नदी"],
        "correct_id": 0,
        "lang": "hindi",
        "explanation": "💡 चीन में बहने वाली यांग्त्सी (Yangtze) नदी चीन के साथ-साथ पूरे एशिया महाद्वीप की सबसे लंबी नदी है।"
    },
    {
        "question": "Who is considered the father of the 'Green Revolution' in India?\n\n[SSC GD 11-Jan-2023 Shift-1]",
        "options": ["Verghese Kurien", "M.S. Swaminathan", "Sam Pitroda", "Norman Borlaug"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 M.S. Swaminathan is considered the father of the Green Revolution in India, whereas Norman Borlaug is known as its father globally."
    },
    {
        "question": "In which state of India is the Lonar Lake situated?\n\n[SSC MTS 05-May-2023 Shift-3]",
        "options": ["Gujarat", "Rajasthan", "Maharashtra", "Odisha"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Lonar Lake, located in the Buldhana district of Maharashtra, is a crater lake formed by a meteorite impact."
    },
    {
        "question": "Which is the leading coal-producing state in India?\n\n[SSC CHSL 15-Mar-2023 Shift-4]",
        "options": ["Jharkhand", "Chhattisgarh", "Odisha", "West Bengal"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 In terms of coal production, Chhattisgarh is a leading state, while Jharkhand holds the largest coal reserves in India."
    },
    {
        "question": "Where is the Sariska National Park located?\n\n[SSC GD 17-Jan-2023 Shift-1]",
        "options": ["Madhya Pradesh", "Uttar Pradesh", "Gujarat", "Rajasthan"],
        "correct_id": 3,
        "lang": "english",
        "explanation": "💡 The Sariska Tiger Reserve is located in the Alwar district of the state of Rajasthan."
    },
    {
        "question": "On which river is the Dhuandhar Waterfalls located?\n\n[SSC MTS 11-May-2023 Shift-1]",
        "options": ["Narmada River", "Tapi River", "Godavari River", "Mahanadi River"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 The Dhuandhar Falls is a famous waterfall located on the Narmada river in Jabalpur, Madhya Pradesh."
    },
    {
        "question": "Which is the largest desert in the world?\n\n[SSC CHSL 13-Mar-2023 Shift-2]",
        "options": ["Thar", "Sahara", "Gobi", "Kalahari"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Sahara Desert, located on the African continent, is the largest hot desert in the world."
    },
    {
        "question": "On which river is the Tehri Dam built?\n\n[SSC GD 24-Jan-2023 Shift-4]",
        "options": ["Alaknanda", "Bhagirathi", "Mandakini", "Yamuna"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 The Tehri Dam, built on the Bhagirathi river in Uttarakhand, is the highest dam in India."
    },
    {
        "question": "Which state in India experiences the earliest sunrise?\n\n[SSC MTS 19-May-2023 Shift-1]",
        "options": ["Assam", "Nagaland", "Arunachal Pradesh", "Manipur"],
        "correct_id": 2,
        "lang": "english",
        "explanation": "💡 Due to its geographical position as the easternmost state of India, Arunachal Pradesh experiences the first sunrise."
    },
    {
        "question": "In which Indian state is the Chilika Wildlife Sanctuary located?\n\n[SSC GD 03-Feb-2023 Shift-1]",
        "options": ["West Bengal", "Odisha", "Andhra Pradesh", "Tamil Nadu"],
        "correct_id": 1,
        "lang": "english",
        "explanation": "💡 Chilika Lake and its associated sanctuary areas are located in the state of Odisha, famous for migratory birds."
    },
    {
        "question": "Which is the longest river in Asia?\n\n[SSC CHSL 17-Mar-2023 Shift-3]",
        "options": ["Yangtze River", "Ganga River", "Indus River", "Mekong River"],
        "correct_id": 0,
        "lang": "english",
        "explanation": "💡 The Yangtze river flowing in China is the longest river in the country as well as the entire continent of Asia."
    },
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
