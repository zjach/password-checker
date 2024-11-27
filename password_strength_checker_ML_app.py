import streamlit as st
import joblib
import numpy as np
import math

# Load the ML model
ml_model = joblib.load('password_strength_model.pkl')

# Feature extraction function for ML
def extract_features(password):
    length = len(password)
    has_upper = int(any(char.isupper() for char in password))
    has_digit = int(any(char.isdigit() for char in password))
    has_special = int(any(char in "!@#$%^&*()-_=+{}[]|\\;:'\",.<>?/~`" for char in password))
    entropy = -sum(password.count(char)/length * math.log2(password.count(char)/length) for char in set(password))
    return np.array([[length, has_upper, has_digit, has_special, entropy]])

# Streamlit app
st.title("Password Strength Checker with ML")

password = st.text_input("Enter your password:")

if st.button("Check Strength"):
    if password:
        # Rule-based checks
        length = len(password)
        has_upper = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in "!@#$%^&*()-_=+{}[]|\\;:'\",.<>?/~`" for char in password)
        
        st.subheader("Rule-Based Results:")
        st.write(f"Length: {length}")
        st.write(f"Contains Uppercase: {'Yes' if has_upper else 'No'}")
        st.write(f"Contains Digit: {'Yes' if has_digit else 'No'}")
        st.write(f"Contains Special Character: {'Yes' if has_special else 'No'}")
        
        # ML prediction
        features = extract_features(password)
        prediction = ml_model.predict(features)[0]
        labels = {0: "Weak", 1: "Moderate", 2: "Strong"}
        
        st.subheader("ML-Based Prediction:")
        st.write(f"Password Strength: **{labels[prediction]}**")
    else:
        st.warning("Please enter a password.")
