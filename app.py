import streamlit as st

#Crop recommendation logic
 
def recommend_crop(N, P, K, temp, humidity, ph, rainfall):
    if rainfall > 150 and 5.0 < ph < 7.5 and N > 50 and humidity > 70:
        return "🌾 Rice"
    elif rainfall < 80 and N > 70 and temp < 25 and ph > 6.0:
        return "🌾 Wheat"
    elif temp > 25 and humidity > 60 and N > 40 and rainfall > 60:
        return "🌽 Maize"
    elif P > 60 and K > 40 and temp < 25 and rainfall > 60:
        return "🥔 Potato"
    elif N > 90 and rainfall > 100 and humidity > 70 and temp > 20:
        return "🎋 Sugarcane"
    elif N < 30 and P > 50 and rainfall > 80 and temp > 20:
        return "🌱 Soybean"
    elif K > 80 and ph > 7.0 and temp > 20 and humidity < 70:
        return "☁️ Cotton"
    elif temp > 30 and humidity > 75 and rainfall > 150 and ph < 7.0:
        return "🍌 Banana"
    elif temp > 20 and temp < 30 and P > 40 and K > 50 and rainfall > 60:
        return "🍅 Tomato"
    elif ph > 5.5 and ph < 7.0 and temp > 15 and temp < 28 and rainfall > 50 and N > 30:
        return "🧅 Onion"
    elif temp > 25 and temp < 35 and humidity > 50 and P > 30 and rainfall < 120:
        return "🌶️ Chilli"
    elif K > 60 and temp > 25 and humidity > 60 and rainfall > 80 and ph < 6.5:
        return "🍠 Sweet Potato"
    elif N > 60 and temp > 18 and temp < 27 and ph > 5.5 and rainfall > 100:
        return "☕ Coffee"
    elif humidity > 80 and rainfall > 200 and temp > 25 and ph < 6.0:
        return "🍵 Tea"
    elif temp > 20 and temp < 30 and K > 40 and ph > 6.0 and rainfall > 50:
        return "🥜 Groundnut"
    elif N < 40 and K > 30 and temp > 25 and humidity < 60 and rainfall < 80:
        return "🌻 Sunflower"
    elif temp > 22 and ph > 6.0 and ph < 7.5 and P > 35 and humidity > 55:
        return "🍇 Grapes"
    else:
        return "🧑‍🌾 Consult Expert"


#Ideal parameters per crop

CROP_PRESETS = {
    "🌾 Rice":         dict(N=80,  P=40,  K=40,  temp=26.0, humidity=80, ph=6.5,  rainfall=200),
    "🌾 Wheat":        dict(N=80,  P=40,  K=40,  temp=22.0, humidity=55, ph=6.5,  rainfall=70),
    "🌽 Maize":        dict(N=60,  P=40,  K=40,  temp=28.0, humidity=65, ph=6.0,  rainfall=90),
    "🥔 Potato":       dict(N=50,  P=70,  K=60,  temp=22.0, humidity=65, ph=5.5,  rainfall=80),
    "🎋 Sugarcane":    dict(N=100, P=40,  K=40,  temp=26.0, humidity=75, ph=6.5,  rainfall=150),
    "🌱 Soybean":      dict(N=20,  P=60,  K=40,  temp=25.0, humidity=65, ph=6.0,  rainfall=100),
    "☁️ Cotton":       dict(N=50,  P=40,  K=90,  temp=28.0, humidity=60, ph=7.2,  rainfall=70),
    "🍌 Banana":       dict(N=60,  P=40,  K=50,  temp=32.0, humidity=80, ph=6.2,  rainfall=180),
    "🍅 Tomato":       dict(N=50,  P=50,  K=60,  temp=25.0, humidity=60, ph=6.2,  rainfall=80),
    "🧅 Onion":        dict(N=40,  P=40,  K=40,  temp=22.0, humidity=60, ph=6.2,  rainfall=60),
    "🌶️ Chilli":      dict(N=50,  P=40,  K=40,  temp=30.0, humidity=60, ph=6.0,  rainfall=90),
    "🍠 Sweet Potato": dict(N=50,  P=40,  K=70,  temp=28.0, humidity=65, ph=6.0,  rainfall=100),
    "☕ Coffee":       dict(N=70,  P=40,  K=40,  temp=23.0, humidity=70, ph=6.0,  rainfall=130),
    "🍵 Tea":          dict(N=50,  P=40,  K=40,  temp=28.0, humidity=85, ph=5.5,  rainfall=220),
    "🥜 Groundnut":    dict(N=30,  P=40,  K=50,  temp=26.0, humidity=55, ph=6.5,  rainfall=70),
    "🌻 Sunflower":    dict(N=30,  P=40,  K=40,  temp=28.0, humidity=50, ph=6.5,  rainfall=60),
    "🍇 Grapes":       dict(N=50,  P=45,  K=50,  temp=26.0, humidity=60, ph=6.5,  rainfall=70),
}


#Page configuration
st.set_page_config(page_title="AgroGuide", page_icon="🌍", layout="wide")

#CSS
st.markdown("""
<style>
.main { background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%); }
.stSlider > div > div > div > div { background: #4CAF50; }

/* Main recommend button */
.stButton > button {
    background: #2E7D32; color: white;
    border-radius: 25px; font-size: 16px; height: 46px;
}

/* AgroGuide brand */
.agroguide-brand {
    display: flex; align-items: center; gap: 8px;
    padding: 4px 0 18px 0;
    border-bottom: 2px solid #4CAF50;
    margin-bottom: 18px;
}
.agroguide-brand .logo    { font-size: 28px; line-height: 1; }
.agroguide-brand .name    { font-size: 20px; font-weight: 700; color: #1B5E20; letter-spacing: -0.3px; }
.agroguide-brand .tagline { font-size: 10px; color: #66BB6A; letter-spacing: 0.8px; text-transform: uppercase; }

/* Sidebar crop buttons */
div[data-testid="stSidebar"] .stButton > button {
    background: #f1f8f1; color: #2E7D32;
    border: 1.5px solid #4CAF50; border-radius: 20px;
    font-size: 14px; height: 38px; width: 100%; margin-bottom: 4px;
}
div[data-testid="stSidebar"] .stButton > button:hover {
    background: #c8e6c9; color: #1B5E20;
}

/* Section heading pill */
.col-heading {
    font-size: 1rem;
    font-weight: 700;
    color: #1B5E20;
    background: #d6edd6;
    border-radius: 10px;
    padding: 0.45rem 0.9rem;
    margin-bottom: 1.1rem;
    display: inline-block;
}

/* Result section heading */
.result-heading {
    font-size: 1rem;
    font-weight: 700;
    color: white;
    background: #2E7D32;
    border-radius: 10px;
    padding: 0.45rem 0.9rem;
    margin-bottom: 1.1rem;
    display: inline-block;
}

/* Result section wrapper */
.result-section {
    background: #f0faf0;
    border: 2px solid #a5d6a7;
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    margin-top: 1.2rem;
}

h1 { margin-bottom: 0 !important; padding-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

#session state
defaults = dict(N=60, P=50, K=55, temp=26.0, humidity=65, ph=6.5, rainfall=110)
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

if "result" not in st.session_state:
    st.session_state.result = None


#Sidebar for crops
with st.sidebar:
    st.markdown("""
    <div class="agroguide-brand">
        <div class="logo">🌍</div>
        <div style="display:flex;flex-direction:column;line-height:1.1">
            <span class="name">AgroGuide</span>
            <span class="tagline">Smart Crop Advisor</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**📋 How to use**")
    st.write("**Step 1**: Click a crop to load its ideal parameters")
    st.write("**Step 2**: Fine-tune sliders to enter your soil & climate conditions")
    st.write("**Step 3**: Click Recommend")
    st.markdown("---")
    st.markdown("**Click a crop to auto-fill sliders:**")

    for crop_name, preset in CROP_PRESETS.items():
        if st.button(crop_name, key=f"btn_{crop_name}"):
            for param, value in preset.items():
                st.session_state[param] = value
            st.session_state.result = None
            st.rerun()


#Page header
st.markdown("""
<div style='text-align:center; padding: 0.4rem 0 0.8rem 0'>
  <h1 style='color:#2E7D32; font-size:2.4rem; margin:0'>🌾 AgroGuide</h1>
  <p style='color:#555; font-size:1rem; margin:0'>Get the perfect crop for your soil & climate</p>
</div>
""", unsafe_allow_html=True)

#Two slider columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<span class="col-heading">🌱 Soil Nutrients</span>', unsafe_allow_html=True)
    N = st.slider("Nitrogen (N)",   0,   200, key="N")
    P = st.slider("Phosphorus (P)", 0,   150, key="P")
    K = st.slider("Potash (K)",     0,   200, key="K")

with col2:
    st.markdown('<span class="col-heading">🌤️ Weather & Soil</span>', unsafe_allow_html=True)
    temp     = st.slider("Temperature (°C)", 0.0, 50.0, key="temp")
    humidity = st.slider("Humidity (%)",     0,   100,  key="humidity")
    ph       = st.slider("pH",              0.0,  14.0, key="ph")
    rainfall = st.slider("Rainfall (mm)",    0,   300,  key="rainfall")

#Recommend button
st.markdown("<div style='margin-top: 1rem'>", unsafe_allow_html=True)
if st.button("🚀 Recommend Best Crop", use_container_width=True):
    st.session_state.result = recommend_crop(N, P, K, temp, humidity, ph, rainfall)
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

#Result section
st.markdown("<div style='margin-top: 1rem'>", unsafe_allow_html=True)

if st.session_state.result:
    result    = st.session_state.result
    is_expert = result == "🧑‍🌾 Consult Expert"

    if is_expert:
        bg_grad    = "linear-gradient(135deg, #E65100, #F57C00)"
        note       = "Your conditions are unusual — please consult a local agronomist."
        icon_color = "🟠"
    else:
        bg_grad    = "linear-gradient(135deg, #1B5E20, #2E7D32)"
        note       = "This crop is a perfect match for your soil & climate conditions!"
        icon_color = "🟢"

    emoji     = result.split()[0]
    crop_name = " ".join(result.split()[1:])

    #result column
    _, card_col, _ = st.columns([1, 2, 1])
    with card_col:
        st.markdown(f"""
        <div style='text-align:center; padding:2rem 2rem 1.8rem 2rem;
                    background:{bg_grad}; border-radius:22px;'>
            <div style='font-size:0.8rem; font-weight:700; letter-spacing:1.2px;
                        color:rgba(255,255,255,0.7); text-transform:uppercase;
                        margin-bottom:0.8rem'>🚀 Recommended Crop</div>
            <div style='font-size:4rem; line-height:1; margin-bottom:0.5rem'>{emoji}</div>
            <div style='font-size:2rem; font-weight:800; color:white;
                        margin-bottom:0.5rem'>{crop_name}</div>
            <div style='display:inline-block; background:rgba(255,255,255,0.18);
                        border-radius:30px; padding:0.35rem 1rem;
                        font-size:0.85rem; color:rgba(255,255,255,0.92)'>{note}</div>
        </div>
        """, unsafe_allow_html=True)
else:
    _, card_col, _ = st.columns([1, 2, 1])
    with card_col:
        st.markdown("""
        <div style='text-align:center; padding:2rem; background:#f7fbf7;
                    border-radius:22px; border:2px dashed #a5d6a7'>
            <div style='font-size:3rem; margin-bottom:0.5rem'>🌿</div>
            <p style='color:#888; font-size:1rem; margin:0'>
                Set your conditions above and click<br>
                <b style="color:#2E7D32">Recommend Best Crop</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<center><i>AgroGuide — Smart Crop Recommendation</i></center>", unsafe_allow_html=True)

#end
