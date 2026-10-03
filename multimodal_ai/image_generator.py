import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

st.title("AIImage Generator")
@st.cache_resource
def load_model():
    pipe=StableDiffusionPipeline.from_pretrained("segmind/tiny-sd", torch_dtype=torch.float32)
    return pipe

pipe=load_model()
st.caption("Model loaded successfully")

st.session_state.setdefault("generated_images", None)
st.session_state.setdefault("generated_images", None)

prompt = st.text_input("Enter your prompt here", placeholder="A dog wearing sunglasses")

generate = st.button("Generate Image")
