import streamlit as st
import time
st.set_page_config(page_title="ChatBOT UI Demo", page_icon=".")
st.title("ChatBOT UI Demo")

with st.chat_message("user"):
    st.write("Hello, I am a user. I want to chat with you.")

with st.chat_message("assistant"):
    st.write("Hello! I am an AI assistant. How can I help you today?")

user_message = st.chat_input("Enter your message:")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5) 
        st.write(f"You said: {user_message}. But I am just a demo, so I cannot respond intelligently. Please try again later.")