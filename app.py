import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    st.error("API key not found! Please add it to the .env file.")
    st.stop()

# Initialize Hugging Face Inference Client
client = InferenceClient(model="gpt2", token=api_key)

def generate_text(prompt, max_length=100, temperature=0.7):
    """
    Generate text completion using Hugging Face API (InferenceClient).
    Args:
        prompt (str): The input prompt to generate text for.
        max_length (int): Maximum number of tokens to generate.
        temperature (float): Creativity level of the output (higher = more creative).
    Returns:
        str: Generated text.
    """
    try:
        # Pass prompt and parameters to the InferenceClient
        response = client.text_generation(
            prompt,
            max_new_tokens=max_length,
            temperature=temperature,
            do_sample=True,
        )
        return response
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.set_page_config(page_title="Text Completion Bot")
st.title("Text Completion Bot")
st.write("Enter a prompt below, and the bot will complete it for you using the Hugging Face GPT model!")

# Input prompt
prompt = st.text_area("Enter your prompt:", "", label_visibility="visible")
max_length = st.slider("Max length of generated text:", 50, 500, 100)
temperature = st.slider("Creativity (temperature):", 0.0, 1.0, 0.7)

# Generate text
if st.button("Generate Text"):
    if prompt.strip():
        with st.spinner("Generating text..."):
            generated_text = generate_text(prompt, max_length=max_length, temperature=temperature)
        st.subheader("Generated Text:")
        st.text_area("Output:", generated_text, height=200, label_visibility="collapsed")
    else:
        st.warning("Please enter a valid prompt!")
