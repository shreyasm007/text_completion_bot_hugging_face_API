import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    st.error("API key not found! Please add it to the .env file.")
    st.stop()

# Streamlit page configuration
st.set_page_config(page_title="Text Completion Bot", page_icon="🤖", layout="centered")

# Fetch available models from Hugging Face API
def fetch_text_generation_models():
    """
    Fetch models tagged with 'text-generation' from Hugging Face API.
    Returns:
        list: A list of model IDs suitable for text completion.
    """
    try:
        response = requests.get(
            "https://huggingface.co/api/models?pipeline_tag=text-generation",
            timeout=10
        )
        response.raise_for_status()
        models = response.json()
        # Filter out models that are too large for free-tier inference
        filtered_models = [
            model["modelId"] for model in models
            if "gpt" in model["modelId"].lower() or "opt" in model["modelId"].lower() or "bloom" in model["modelId"].lower()
        ]
        return filtered_models[:20]  # Return the top 20 models for simplicity
    except Exception as e:
        st.error(f"Error fetching models from Hugging Face: {e}")
        return ["gpt2", "bigscience/bloom", "EleutherAI/gpt-neo-2.7B"]  # Fallback models

# Get the list of models
MODEL_OPTIONS = fetch_text_generation_models()

def initialize_client(model_name):
    """
    Initialize the InferenceClient with the specified model.
    Args:
        model_name (str): The model repository ID from Hugging Face.
    Returns:
        InferenceClient: An initialized client for the specified model.
    """
    try:
        client = InferenceClient(model=model_name, token=api_key)
        return client
    except Exception as e:
        st.error(f"Error initializing model {model_name}: {e}")
        st.stop()

# Streamlit UI
st.title("🤖 Text Completion Bot")
st.write("Choose a model from Hugging Face and enter a prompt to generate text.")

# Dropdown for model selection
model_name = st.selectbox(
    "Select a model:",
    options=MODEL_OPTIONS,
    index=0,
    help="Choose a Hugging Face model for text generation."
)

# Initialize client with the selected model
client = initialize_client(model_name)

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
        start_time = time.time()
        response = client.text_generation(
            prompt,
            max_new_tokens=max_length,
            temperature=temperature,
            do_sample=True,
        )
        end_time = time.time()
        response_time = end_time - start_time
        return response, response_time
    except Exception as e:
        if "504" in str(e):
            return (
                f"Error: The selected model ({model_name}) is too large or timed out. "
                f"Try using a smaller model like 'gpt2' or 'bigscience/bloom'.", 
                None
            )
        elif "403" in str(e):
            return (
                f"Error: Access forbidden for the model ({model_name}). "
                f"This might be due to size limitations. Please try a different model.", 
                None
            )
        return f"Error: {e}", None

# Input prompt
prompt = st.text_area("Enter your prompt:", "", label_visibility="visible")
max_length = st.slider("Max length of generated text:", 10, 500, 100)  # Min set to 10
temperature = st.slider("Creativity (temperature):", 0.0, 1.0, 0.7)

# Generate text
if st.button("Generate Text"):
    if prompt.strip():
        with st.spinner(f"Generating text using {model_name}..."):
            generated_text, response_time = generate_text(
                prompt, max_length=max_length, temperature=temperature
            )
        
        if "Error" in generated_text:
            st.error(generated_text)
        else:
            st.subheader("Generated Text:")
            st.text_area("Output:", generated_text, height=200, label_visibility="collapsed")
            st.info(f"Response Time: {response_time:.2f} seconds")
    else:
        st.warning("Please enter a valid prompt!")
