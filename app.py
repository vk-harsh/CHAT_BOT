import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ Set page config
st.set_page_config(page_title="AGENT")

# ✅ Background image CSS
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.pixabay.com/photo/2024/04/09/15/45/ai-generated-8686233_1280.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            opacity: 0.3;
        }

        /* Remove black bars from input, text area, buttons */
        .stTextInput>div>div>input,
        .stTextArea>div>textarea,
        .stButton>button {
            background-color: rgba(0, 0, 0, 0.3); /* Slightly transparent */
            color: white;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>textarea:focus {
            border: 1px solid #00c0ff;
            outline: none;
        }

        .stButton>button:hover {
            background-color: rgba(0, 0, 0, 0.5);
        }

        .chat-container {
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            padding: 20px;
            max-height: 600px;
            overflow-y: auto;
        }

        .user-msg {
            background-color: rgba(31, 119, 180, 0.8);
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: right;
        }

        .bot-msg {
            background-color: rgba(44, 160, 44, 0.8);
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
        }

        .input-container {
            margin-top: 20px;
        }

        h1, h2, h3, h4, h5, h6, p, div {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


set_background()

# ✅ Load env and model
load_dotenv()
genai.configure(api_key="AIzaSyB_RYhSdu7p0z4XgcfDnubkFMpC8ksdlyE")
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# ✅ App UI in visible container
st.markdown("<h1 style='text-align: center; color: white;'>🤖AGENT</h1>", unsafe_allow_html=True)
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
