import streamlit as st
from llm import get_response
from ui import setup_ui
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Setup UI
setup_ui()

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]

# Show welcome message
if len(st.session_state.messages) == 1:
    st.info("Start chatting with MIKA 🚀")

# Display chat history (skip system message)
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue

    with st.chat_message(
        msg["role"],
        avatar="🧑" if msg["role"] == "user" else "🤖"
    ):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask anything about AI, coding, or tech...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Show user message instantly
    with st.chat_message("user", avatar="🧑"):
        st.write(user_input)

    # Get AI response
    reply = get_response(st.session_state.messages)

    # Typing animation (clean implementation)
    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        full_response = ""

        for chunk in reply.split():
            full_response += chunk + " "
            time.sleep(0.02)
            placeholder.markdown(full_response)

    # Save assistant message AFTER rendering
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )