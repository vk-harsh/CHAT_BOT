import streamlit as st
import base64
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ✅ Must be first Streamlit command
st.set_page_config(page_title="AGENT")

# Load environment and configure Gemini
load_dotenv()
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# ✅ Convert your uploaded image to base64
with open("/mnt/data/background.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

# ✅ Set background CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{encoded}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

h1 {{
    font-size: 4rem !important;
    text-align: center;
    color: white;
    text-shadow: 2px 2px 4px #000;
}}

input[type="text"] {{
    font-size: 20px !important;
    height: 50px !important;
}}
</style>
"""

# ✅ Inject CSS and run app
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1>AGENT</h1>", unsafe_allow_html=True)

input = st.text_input("Ask Anything", key="input")
submit = st.button("Ask your query")

if submit:
    response = my_output(input)
    st.subheader("The Response is:")
    st.write(response)
