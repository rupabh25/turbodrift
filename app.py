import streamlit as st
from auth import create_db, login_user, signup_user

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Turbo Drift",
    page_icon="🚗"
)

# ---------- CREATE DATABASE ----------
create_db()

# ---------- TITLE ----------
st.title("🚗 Turbo Drift")

# ---------- MENU ----------
menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------- SIGNUP ----------
if choice == "Signup":

    st.subheader("Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Signup"):

        if new_user and new_pass:

            result = signup_user(new_user, new_pass)

            if result:
                st.success("✅ Account created! Go to Login.")
            else:
                st.error("❌ Username already exists")

        else:
            st.warning("⚠️ Enter username and password")

# ---------- LOGIN ----------
elif choice == "Login":

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = login_user(username, password)

        if user:

            st.session_state["logged_in"] = True
            st.session_state["username"] = username

            st.success(f"✅ Welcome {username}!")
            st.balloons()

            st.switch_page("pages/1_Predict_Price.py")

        else:
            st.error("❌ Invalid login")