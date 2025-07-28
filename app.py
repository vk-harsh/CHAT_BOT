import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ Set page config
st.set_page_config(page_title="AGENT")

# ✅ Background image CSS
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.pixabay.com/photo/2024/04/09/15/45/ai-generated-8686233_1280.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .input-container {
            background: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 15px;
            max-width: 600px;
            margin: 0 auto;
            margin-top: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# ✅ Load env and model
load_dotenv()
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# ✅ App UI in visible container
st.markdown("<h1 style='text-align: center; color: white;'>AGENT</h1>", unsafe_allow_html=True)
st.markdown("<div class='input-container'>", unsafe_allow_html=True)

input = st.text_input("Ask Anything", key="input")
submit = st.button("Ask your query")

st.markdown("</div>", unsafe_allow_html=True)

if submit:
    response = my_output(input)
    st.markdown("<div style='background-color: rgba(0,0,0,0.6); padding: 1rem; border-radius: 10px;'>", unsafe_allow_html=True)
    st.subheader("The Response is:", divider="gray")
    st.write(response)
    st.markdown("</div>", unsafe_allow_html=True)
