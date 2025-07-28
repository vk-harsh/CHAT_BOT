import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ First line for Streamlit config
st.set_page_config(page_title="AGENT")

# ✅ Set background with overlay opacity
def set_background_image():
    st.markdown(
        """
        <style>
        body {
            margin: 0;
        }

        .stApp {
            position: relative;
            z-index: 0;
        }

        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("https://cdn.pixabay.com/photo/2024/04/09/15/45/ai-generated-8686233_1280.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            opacity: 0.3;
            z-index: -1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# ✅ Load Gemini
load_dotenv()
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# ✅ UI
st.markdown("<h1 style='text-align: center; color: white;'>AGENT</h1>", unsafe_allow_html=True)

input = st.text_input("Ask Anything", key="input")
submit = st.button("Ask your query")

if submit:
    response = my_output(input)
    st.subheader("The Response is:")
    st.write(response)
