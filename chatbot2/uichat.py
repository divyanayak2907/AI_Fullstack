from ollama import chat
import streamlit as st

st.set_page_config(page_title="LlamaBot App", page_icon="🤖")
st.title("LlamaBot ")

personality = " you are a friendly and patient tutor name Llama .answer warmly .keep the answer in one sentence "
personality2="you are a lawyer name joseph   \
    and give the answer in one sentence and professional"
if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": personality}]
    if "toast_msg" not in st.session_state:
        st.session_state.toast_msg = None
    
    if st.session_state.toast_msg:
        st.toast(st.session_state.toast_msg[0],st.session_state.toast_msg[1])
        st.session_state.toast_msg = None

with st.sidebar:
    st.header("Chat Controls")
    if st.button("Clear Chat", type="primary"):
        st.session_state.history = [{"role": "system", "content": personality}]
        st.session_state.toast_msg = ("Chat cleared!", "success",)
        st.rerun()
    if st.button("Change Personality"):
        st.session_state.history[0]["content"]= personality2
        st.session_state.toast_msg = ("Personality changed!")
        st.rerun()

with st.chat_message("assistant"):
    st.write("Hello! I am Llama, your friendly tutor. How can I assist you today?")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask Anything", key="input")
if question :
    st.session_state.history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)
    try:
        with st.spinner("Thinking..."):
            response = chat(model="llama3.2", messages=st.session_state.history)
        reply = response.message.content
        st.session_state.history.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.wriite("ollama is not working! Try again Later")
