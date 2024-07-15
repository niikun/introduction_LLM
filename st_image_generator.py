#!/workspaces/introduction_LLM/.venv/bin/python

import os
from dotenv import load_dotenv
import streamlit as st
import openai

load_dotenv(verbose=True)

def get_image(input):
    """
    Generating image from prompt using OpenAI's DALL-E model
    """

    openai.api_key = os.environ["OPENAI_API_KEY"]
    response = openai.Image.create(
        prompt=input,
        n=1,
        size="1024x1024"
    )

    return response['data'][0]['url']

st.title("Image Generator")
st.write("This app generates images from text prompts using OpenAI's DALL-E model")
st.write("Enter a prompt and click the button to generate an image")
prompt = st.text_input("Prompt")
if st.button("Generate Image"):
    with st.spinner("Generating Image..."):
        image_url = get_image(prompt)
        st.image(image_url)
