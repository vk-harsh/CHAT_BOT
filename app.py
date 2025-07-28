from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

st.set_page_config(page_title="AGENT", layout="centered")

background_image_url = "https://github.com/vk-harsh/CHAT_BOT/blob/e337c620475c9b400671e38465e690ad002e7bd2/bg.png"
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.95;
    }}
    .title-style {{
        color: #ffffff;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        padding-top: 30px;
    }}
    .textbox-style input {{
        background-color: #ffffff33;
        color: white;
        font-size: 18px;
    }}
    .stButton button {{
        background-color: #008CBA;
        color: white;
        font-size: 18px;
        border-radius: 8px;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-style">AGENT</div>', unsafe_allow_html=True)
input = st.text_input("Input", key="input")
submit = st.button("Ask your query")

if submit:
    response = my_output(input)
    st.subheader("The Response is:")
    st.write(response)
