import re
import random
import string
import streamlit as st  # type: ignore

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Common weak passwords to avoid
    common_passwords = ["password", "123456", "qwerty", "password123", "admin"]
    if password.lower() in common_passwords:
        return "❌ Very Weak Password! Avoid using common passwords.", 0
    
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters for better security.")
    
    # Check for numeric digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one numeric digit (0-9) to enhance strength.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*) to improve security.")
    
    # Determine password strength
    if score == 4:
        return "✅ Strong Password! Your password has been saved.", score
    elif score == 3:
        return "⚠ Moderate Password - Consider adding more security features.", score
    else:
        return "\n".join(feedback) + "\n❌ Weak Password - Strengthen it using the suggestions above.", score

# Function to generate a strong password
def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="\U0001F512", layout="centered")

# Apply custom styling with CSS
st.markdown("""
    <style>
        html, body, [class*="stApp"] {
            background: linear-gradient(to right, #2C3E50, #4CA1AF);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 64px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 10px;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .footer {
            text-align: center;
            font-size: 18px;
            margin-top: 50px;
            color: #ffffff;
            font-weight: bold;
        }
        .linkedin-logo {
            display: flex;
            justify-content: center;
            margin-top: 5px;
        }
        .stButton>button {
            background-color: #4CA1AF !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            border: none !important;
            cursor: pointer !important;
        }
        .strong-password-suggestion {
            color: white !important;
            font-weight: bold;
            animation: blink 1s infinite;
        }
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<h1 class="title">\U0001F512 Password Strength Meter</h1>', unsafe_allow_html=True)

# Password input field
password = st.text_input("Enter Password", type="password")

# Analyze password button
if st.button("Tap To Analyze"):
    if password:
        result, score = check_password_strength(password)
        
        if score == 4:
            st.success("✅ Your strong password has been saved securely!")
            st.markdown(f'<p class="title">{result}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="weak-password">{result}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="strong-password-suggestion">🔑 Suggested Strong Password: {generate_strong_password()}</p>', unsafe_allow_html=True)
    else:
        st.error("Please enter a password!")

# Footer with LinkedIn link
st.markdown('<div class="footer">Prepared By Bilal Waseem</div>', unsafe_allow_html=True)
st.markdown('<div class="linkedin-logo"><a href="https://www.linkedin.com/in/bilal-waseem-b44006338" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="40"></a></div>', unsafe_allow_html=True)
