import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# Page setup
st.set_page_config(page_title="AGENT", page_icon="🤖", layout="centered")

# Background image
st.markdown("""
    <style>
    .stApp {
        background-image: url('bg.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: left top;
    }
    .overlay {
        background-color: rgba(0, 0, 0, 0.5);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    </style>
    <div class="overlay"></div>
""", unsafe_allow_html=True)

# UI Content
st.title("🤖 AGENT")
query = st.text_area("Enter your query:")
if st.button("Get Response"):
    response = my_output(query)
    st.subheader("Response:")
    st.write(response)
