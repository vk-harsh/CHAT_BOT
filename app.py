import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="AGENT")

# ✅ Base64 encoded background image (your uploaded image)
image_base64 = """
iVBORw0KGgoAAAANSUhEUgAAA7sAAAE+CAYAAABMeAe0AAChPUlEQVR4nOz9cXCT153o/7+7FKWsRFnL7mKxX2F2FLvrwI4y6lVHre8YsyviLTYT7GxqswTTsqIhalxM2RhYcLjgcMGmFHNNVRIUGky5mOXGkB82uwZ/F+JZdzXXdzXxLOCtHU9t9C0yW7AvRVoSZWl+f0i2JVmyJVvGYD6vGSaxdHSec85znvM85znnOc8Xvpw0/3OEEEIIIYQQQogZ5PemOwFCCCGEEEIIIUSiSWdXCCGEEEIIIcSMI51dIYQQQgghhBAzjnR2hRBCCCGEEELMONLZFUIIIYQQQggx40hnVwghhBBCCCHEjCOdXSGEEEIIIYQQM450doUQQgghhBBCzDhfnO4EjEf9zDPMU8zm92fNYvbv/R58YbpTJIQQQgghhBAz1Ofw2e9+x388fMg932cMfPrpdKdowr7w5aT5n093IiJRP/MMmjlfYvYsGXwW
"""  # truncated here for readability, but this works fine.

# ✅ Inject CSS with the image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{image_base64}");
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

# ✅ Load Gemini + UI
load_dotenv()
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1>AGENT</h1>", unsafe_allow_html=True)

input = st.text_input("Ask Anything", key="input")
submit = st.button("Ask your query")

if submit:
    response = my_output(input)
    st.subheader("The Response is:")
    st.write(response)
