import streamlit as st

st.set_page_config(page_title="Kingmaker Health Chatbot", page_icon="🩺", layout="centered")
st.title("🩺 Kingmaker Health Chatbot (Demo)")

# Step 1: Language selection
language = st.selectbox("Choose Language / भाषा चुनें:", ["English", "Hindi"])

if language == "English":
    st.write("This demo gives health & diet awareness for **Youth, Women, and Diabetes patients**.")
    category = st.selectbox("Choose your category:", ["Youth", "Women", "Diabetes"])

    if category == "Youth":
        st.subheader("👦 Youth Health & Diet Suggestions")
        st.write("""
        ✅ What to eat:
        - Breakfast: Oats, milk, fruits
        - Lunch: Chapatis, dal, salad, vegetables
        - Evening: Nuts, sprouts, green tea
        - Dinner: Paneer, vegetables, light food

        ❌ Avoid:
        - Junk food, soft drinks, excess sugar
        - Skipping meals

        💡 Tips:
        - Exercise 30 mins daily
        - Sleep 7–8 hours
        - Stay hydrated
        """)
    elif category == "Women":
        st.subheader("👩 Women Health & Period Awareness")
        st.write("""
        ✅ Eat:
        - Iron-rich foods: spinach, beetroot, jaggery
        - Warm water, herbal tea

        ❌ Avoid:
        - Cold drinks, spicy/oily food, excess caffeine

        💡 Tips:
        - Light yoga/stretching for cramps
        - Proper rest & hygiene
        """)
    elif category == "Diabetes":
        st.subheader("🩺 Diabetes Patients – Food Awareness")
        st.write("""
        ✅ Eat:
        - Multigrain roti, dal, salad, leafy vegetables
        - Pulses, sprouts, nuts (in moderation)

        ❌ Avoid:
        - White rice, sweets, fried food, sugary drinks

        💡 Tips:
        - Small frequent meals
        - 30 mins walking daily
        - Monitor blood sugar
        """)

elif language == "Hindi":
    st.write("यह डेमो चैटबॉट **युवा, महिलाएँ और डायबिटीज़ मरीजों** के लिए स्वास्थ्य और खान-पान की जानकारी देता है।")
    category = st.selectbox("अपनी श्रेणी चुनें:", ["युवा", "महिलाएँ", "डायबिटीज़ मरीज"])

    if category == "युवा":
        st.subheader("👦 युवाओं के लिए स्वास्थ्य और डाइट सुझाव")
        st.write("""
        ✅ क्या खाएँ:
        - नाश्ता: ओट्स, दूध, फल
        - दोपहर का खाना: 2 रोटी, दाल, सलाद, सब्ज़ियाँ
        - शाम: मेवे, अंकुरित अनाज, ग्रीन टी
        - रात: पनीर, हल्का भोजन

        ❌ क्या न खाएँ:
        - जंक फूड, कोल्ड ड्रिंक्स, ज़्यादा चीनी
        - भोजन छोड़ना

        💡 सुझाव:
        - रोज़ 30 मिनट व्यायाम करें
        - 7–8 घंटे की नींद लें
        - पर्याप्त पानी पिएँ
        """)
    elif category == "महिलाएँ":
        st.subheader("👩 महिलाओं के लिए स्वास्थ्य और पीरियड जागरूकता")
        st.write("""
        ✅ क्या खाएँ:
        - आयरन से भरपूर भोजन: पालक, चुकंदर, गुड़
        - गुनगुना पानी, हर्बल चाय

        ❌ क्या न खाएँ:
        - ठंडे पेय, आइसक्रीम
        - मसालेदार/तला हुआ खाना
        - ज़्यादा कैफ़ीन

        💡 सुझाव:
        - हल्का योग / स्ट्रेचिंग
        - आराम और नींद
        - सफाई और हाइजीन
        """)
    elif category == "डायबिटीज़ मरीज":
        st.subheader("🩺 डायबिटीज़ मरीजों के लिए खान-पान")
        st.write("""
        ✅ क्या खाएँ:
        - मल्टीग्रेन रोटी, दाल, सलाद
        - हरी पत्तेदार सब्ज़ियाँ
        - दालें और अंकुरित अनाज
        - मेवे (सीमित मात्रा में)

        ❌ क्या न खाएँ:
        - सफ़ेद चावल, मिठाई, तला-भुना खाना
        - सॉफ्ट ड्रिंक, पैकेज्ड जूस

        💡 सुझाव:
        - थोड़े-थोड़े करके खाएँ
        - रोज़ 30 मिनट पैदल चलें
        - नियमित रूप से शुगर जाँचें
        """)
