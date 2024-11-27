import streamlit as st
import math
import re

# Function to calculate password entropy
def calculate_entropy(password):
    length = len(password)
    charset_size = 0

    if re.search(r'[a-z]', password):
        charset_size += 26  # Lowercase letters
    if re.search(r'[A-Z]', password):
        charset_size += 26  # Uppercase letters
    if re.search(r'\d', password):
        charset_size += 10  # Numbers
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32  # Special characters

    if charset_size == 0:
        return 0  # Avoid division by zero

    return round(length * math.log2(charset_size), 2)

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Entropy calculation
    entropy = calculate_entropy(password)

    # Rules-based scoring
    score = 0
    if length >= 8:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, entropy

# Streamlit app
st.title("Password Strength Checker")
st.write("Welcome to the Password Strength Checker!")
st.write("Enter a password to evaluate its strength based on length, character types, and entropy.")

# Input for password
password = st.text_input("Enter a password to check:")

# Add a button with a unique key for checking password strength
if st.button("Check Strength", key="check_strength"):
    if password:
        # Check strength
        strength, entropy = check_password_strength(password)
        st.write(f"**Password Strength:** {strength}")
        st.write(f"**Password Entropy:** {entropy} bits")
    else:
        st.warning("Please enter a password to check.")

# Add a fallback message with a unique key
if st.button("App Running Message", key="fallback_message"):
    st.write("App is running. Please enter a password and click 'Check Strength'.")
