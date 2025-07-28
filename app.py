from dotenv import load_dotenv 
load_dotenv() 
import streamlit as st 
import os 
import google.generativeai as genai 

# Configure Gemini API
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash") 

# Function to get model response
def my_output(query):
    response = model.generate_content(query) 
    return response.text 

# Streamlit Page Config
st.set_page_config(
    page_title="AGENT",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for background and styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
        font-family: 'Courier New', monospace;
    }
    .stTextInput > div > div > input {
        color: black;
        font-weight: bold;
    }
    .response-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        color: #d1d5db;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center;'>🤖 AGENT</h1>", unsafe_allow_html=True)

# Input box (textarea for multiline support)
query = st.text_area("Enter your query here 👇", height=100)

# Submit button
if st.button("🚀 Get Response""):
    if query.strip() != "":
        response = my_output(query)
        st.markdown("### 📬 The Response is:")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid query.")
