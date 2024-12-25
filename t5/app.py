import os
import streamlit as st
import requests
import json

# Streamlit app title
st.title("T5 Translation")

# Supported languages
languages = ["English", "French", "German", "Romanian"]

# Dropdowns for source and target languages
source_language = st.selectbox("Select the source language:", languages)
target_language = st.selectbox("Select the target language:", languages)

# Ensure the source and target languages are not the same
if source_language == target_language:
    st.warning("Source and target languages must be different.")

# Text area for user input
prompt_text = st.text_area("Enter the text to translate:")

# Read API URL from environment variables
api_url = os.getenv("API_URL", "http://localhost:80/openai/v1/completions")

headers = {
    "Content-Type": "application/json",
}

# Streamlit button for translation
if st.button("Translate"):
    if prompt_text.strip() and source_language != target_language:
        # Prepare the payload
        payload = {
            "model": "t5",
            "prompt": f"translate {source_language} to {target_language}: {prompt_text}",
            "stream": False,
            "max_tokens": 30,
        }

        # Make the API call
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                # Parse the response
                translation = (
                    response.json()
                    .get("choices", [{}])[0]
                    .get("text", "No translation provided")
                )
                st.success(f"Translation: {translation}")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error while calling the API: {e}")
    else:
        if not prompt_text.strip():
            st.warning("Please enter some text to translate.")
