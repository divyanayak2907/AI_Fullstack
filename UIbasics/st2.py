import streamlit as st
st.set_page_config(page_title="Streamlit Text Input Demo", page_icon=".")
st.title("Streamlit Text Input Demo")

name = st.text_input("Enter your name:",placeholder="Type your name here...")
st.write(f"Hello, {name}!")

password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")
st.write(f"Your password is {len(password)} characters long.")

comments = st.text_area("Enter your comments:", placeholder="Type your comments here...",height=100)
st.write(f"you wrote {len(comments)} characters in your comments.")

if st.button("SUBMIT"):
    st.write("Form submitted successfully!")

show_message = st.checkbox("Do you want extra message?")
if show_message:
    st.write("This is an extra message displayed because you checked the box.,Have a great day!")
    st.write("This is an extra message displayed because you checked the box.,Have a great day!")