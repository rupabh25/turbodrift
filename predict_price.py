import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Turbo Drift",
    page_icon="🚗",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: white !important;
}

p {
    color: #d1d1d1;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    border: none;
    transition: 0.3s;
    font-weight: bold;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

[data-testid="stSidebar"] {
    background-color: #161A23;
}

.metric-card {
    background-color: #1E222D;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- AUTH CHECK ----------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Please login first")
    st.stop()

# ---------- LOGOUT ----------
if st.sidebar.button("Logout"):

    st.session_state["logged_in"] = False
    st.session_state["username"] = ""

    st.switch_page("app.py")

# ---------- LOAD MODEL ----------
try:
    model = joblib.load("car_price_model.pkl")

except Exception as e:
    st.error(f"❌ Model Loading Error: {e}")
    st.stop()

# ---------- TITLE ----------
st.markdown("""
<h1 style='text-align: center; font-size: 52px;'>
🚗 Turbo Drift
</h1>

<h4 style='text-align: center; color: gray;'>
AI Powered Car Price Prediction System
</h4>
""", unsafe_allow_html=True)

# ---------- USER ----------
st.success(f"Welcome, {st.session_state['username']} 👋")

# ---------- ABOUT CARD ----------
st.markdown("""
<div class='metric-card'>
    <h3>About Project</h3>
    <p>
    This Machine Learning application predicts used car prices
    using multiple vehicle parameters such as fuel type,
    transmission, ownership, kilometers driven and car age.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.header("🚘 Enter Car Details")

car_age = st.sidebar.slider(
    "Car Age (Years)",
    0,
    20,
    5
)

kms = st.sidebar.slider(
    "Kilometers Driven",
    0,
    200000,
    50000
)

owners = st.sidebar.selectbox(
    "Number of Owners",
    [0, 1, 2, 3]
)

fuel = st.sidebar.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller = st.sidebar.selectbox(
    "Dealer or Owner",
    ["Dealer", "Individual"]
)

trans = st.sidebar.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

# ---------- SPACING ----------
st.markdown("<br>", unsafe_allow_html=True)

# ---------- PREDICTION ----------
if st.button("🚀 Predict Price"):

    try:

        fuel_map = {
            "Petrol": 2,
            "Diesel": 1,
            "CNG": 0
        }

        seller_map = {
            "Dealer": 0,
            "Individual": 1
        }

        trans_map = {
            "Manual": 1,
            "Automatic": 0
        }

        input_data = pd.DataFrame({
            "Kms_Driven": [kms],
            "Fuel_Type": [fuel_map[fuel]],
            "Seller_Type": [seller_map[seller]],
            "Transmission": [trans_map[trans]],
            "Car_Age": [car_age]
        })

        prediction = model.predict(input_data)

        predicted_price = round(prediction[0], 2)

        st.markdown(f"""
        <div class='metric-card'>
            <h2>💰 Estimated Price</h2>
            <h1>₹ {predicted_price} Lakhs</h1>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")

# ---------- GRAPH ----------
st.subheader("📈 Sample Price Trend")

sample_prices = np.random.randint(
    500000,
    2000000,
    10
)

st.line_chart(sample_prices)

# ---------- FOOTER ----------
st.markdown("---")

st.caption(
    "Developed by: Samarth Pandya, Rupabh Shrivastava, Rudra Patidar | Mini Project 2026"
)