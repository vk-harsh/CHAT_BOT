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
            background-opacity: 0.7;
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
# Securely load the API key from .env file
api_key = os.getenv("GOOGLE_API_KEY") 
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# Initialize chat history state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ App UI in visible container
st.markdown("<h1 style='text-align: center; color: white;'>🤖AGENT</h1>", unsafe_allow_html=True)

# Display chat messages from history inside the styled container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='input-container'>", unsafe_allow_html=True)

# Use st.form so hitting Enter automatically submits the input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask Anything")
    submit = st.form_submit_button("Ask your query")

st.markdown("</div>", unsafe_allow_html=True)

if submit and user_input:
    # 1. Add user message to state
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # 2. Get AI Response
    response_text = my_output(user_input)
    
    # 3. Add AI message to state
    st.session_state["messages"].append({"role": "bot", "content": response_text})
    
    # 4. Rerun to update the UI with new messages
    st.rerun()
