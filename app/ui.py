import streamlit as st

def setup_ui():
    st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0f172a;
            color: white;
        }
        .chat-box {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🤖 MIKA")
    st.caption("Built by Aditya | Generative AI Engineer")
    st.caption("Powered by LLM APIs | Built using Generative AI workflows")
    st.markdown("### 🚀 Your AI Assistant for Learning & Building")

