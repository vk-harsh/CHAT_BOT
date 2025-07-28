import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ Must be first Streamlit command
st.set_page_config(page_title="AGENT")

# ✅ Set background image via URL
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://pixabay.com/photos/coding-computer-hacker-hacking-1841550/");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# ✅ Load environment and configure Gemini
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
