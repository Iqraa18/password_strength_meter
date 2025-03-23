import streamlit as st
import re
import random
import string

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    feedback = []

    # Blacklist Common Passwords
    common_passwords = ["password", "123456", "qwerty", "password123", "admin", "letmein"]
    if password.lower() in common_passwords:
        return "❌ Your password is too common. Choose a more secure one.", "weak"

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "strong"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "moderate"
    else:
        feedback.append(f"🔹 Suggested Strong Password: {generate_strong_password()}")
        return "\n".join(feedback), "weak"

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    message, strength = check_password_strength(password)
    if strength == "strong":
        st.success(message)
    elif strength == "moderate":
        st.warning(message)
    else:
        st.error(message)
