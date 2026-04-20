import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ Page config
st.set_page_config(page_title="AGENT")

# ✅ Background + UI styling
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.pixabay.com/photo/2024/04/09/15/45/ai-generated-8686233_1280.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .stTextInput>div>div>input,
        .stTextArea>div>textarea,
        .stButton>button {
            background-color: rgba(0, 0, 0, 0.3);
            color: white;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        .stTextInput>div>div>input:focus,
        .stTextArea>div>textarea:focus {
            border: 1px solid #00c0ff;
        }

        .stButton>button:hover {
            background-color: rgba(0, 0, 0, 0.5);
        }

        .chat-container {
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            padding: 20px;
            max-height: 500px;
            overflow-y: auto;
        }

        .user-msg {
            background-color: rgba(31, 119, 180, 0.8);
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: right;
        }

        .bot-msg {
            background-color: rgba(44, 160, 44, 0.8);
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
        }

        h1, h2, h3, h4, h5, h6, p, div {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# ✅ Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please add it to your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# ✅ FIXED MODEL (important)
model = genai.GenerativeModel("gemini-2.5-flash")

# ✅ Function to get response
def my_output(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ✅ Chat memory
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ Title
st.markdown("<h1 style='text-align: center;'>🤖 AGENT</h1>", unsafe_allow_html=True)

# ✅ Chat display
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ✅ Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask Anything")
    submit = st.form_submit_button("Ask your query")

# ✅ On submit
if submit and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # 🔄 Show loading spinner
    with st.spinner("Thinking..."):
        response_text = my_output(user_input)

    st.session_state["messages"].append({"role": "bot", "content": response_text})

    st.rerun()