from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

# ✅ Configure API Key (use from .env or directly if testing)
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")

model = genai.GenerativeModel("gemini-2.0-flash")

# ✅ Function to get Gemini response
def my_output(query):
    response = model.generate_content(query)
    return response.text

# ✅ Streamlit Page Config
st.set_page_config(page_title="AGENT", layout="centered")

# ✅ Background Image CSS (you can change this URL to your GitHub raw image)
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("bg.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}
    .stTextInput>div>div>input {{
        background-color: #ffffff11;
        color: white;
        border: 1px solid #ffffff33;
        border-radius: 10px;
        padding: 10px;
    }}
    .stButton>button {{
        background-color: #00b4d8;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }}
    .stButton>button:hover {{
        background-color: #0077b6;
        transition: 0.3s;
    }}
    .stHeader, .stSubheader {{
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ UI Header
st.header("🤖 Welcome to AGENT")

# ✅ Input box
query = st.text_input("Enter your query:", key="input")

# ✅ Submit button
if st.button("Ask your query"):
    with st.spinner("Thinking..."):
        response = my_output(query)
    st.subheader("Response:")
    st.write(response)
