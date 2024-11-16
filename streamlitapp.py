import streamlit as st
import requests


API_URL = "https://usecase-7-vzhx.onrender.com/predict"  


st.markdown("""
    <style>
        body {
            direction: rtl;
            text-align: right;
        }
        .streamlit-expanderHeader {
            text-align: right;
        }
        .stTextInput>div>div>input {
            text-align: right;
        }
        .stMarkdown {
            text-align: right;
        }
        .prediction-output {
            font-size: 18px;
            font-weight: bold;
            text-align: right;
            direction: rtl;
        }       
    </style>
""", unsafe_allow_html=True)

st.title("توقع سعر الاعب في كرة القدم ⚽")
st.markdown("""بحكم ان كرة القدم من اشهر الرياضات في العالم
            , والانتقالات الشتويه جايه ف ودك تعرف ناديك كم ممكن يدفع على الاعب ؟
            , سويت لك مودل يتوقع سعر اللاعب التقريبي بعدة عوامل حطيتها لك تحت وتوقع كم ناديك بيصرف في الشتوية 🥶""")

goals = st.number_input("معدل الاهداف لكل مباره (الموسم الحالي)", min_value=0.0, max_value=1.0)
assists = st.number_input("معدل مساعدة التهديف لكل مباره (الموسم الحالي)", min_value=0.0,max_value=1.0)
minutes_played = st.number_input("عدد الدقائق التي لعبها (الموسم الحالي)  ", min_value=0)
games_injured = st.number_input("المباريات التي غاب عنها بداعي الاصابه", min_value=0)
award = st.number_input("مجموع الجوائز الفرديه ", min_value=0)
highest_value = st.number_input("اعلى قيمة انتقال حققها الاعب (باليورو)", min_value=0)


if st.button("توقع السعر 💵"):

    payload = {
        "goals": float(goals),
        "assists": float(assists),
        "minutes_played": int(minutes_played),
        "games_injured": int(games_injured),
        "award": int(award),
        "highest_value": int(highest_value)
    }
    

    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        prediction = response.json()["pred"]
        prediction_1 = f"{prediction:,.2f}" 
        st.markdown(f'<p class="prediction-output">سعر اللاعب المتوقع هو: {prediction_1} €</p>', unsafe_allow_html=True)
    else:
        st.error("Error making prediction!")