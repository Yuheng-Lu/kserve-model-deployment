import os
import streamlit as st
import requests
import json

# Streamlit app title
st.title("BERT Fill-Mask Prediction")

# Instruction for the user
st.markdown(
    """
Enter sentences with a `[MASK]` token to predict masked words.
Example: `The capital of France is [MASK].`
"""
)

# Text area for user input
mask_sentences = st.text_area("Enter sentences (one per line):")

# Read API URL from environment variables
api_url = os.getenv("API_URL", "http://localhost:80/v1/models/bert:predict")

# Streamlit button for prediction
if st.button("Predict Mask"):
    # Split input into a list of sentences
    sentences = [line.strip() for line in mask_sentences.split("\n") if line.strip()]

    if sentences:
        # Prepare the payload
        payload = {"instances": sentences}

        # Set headers
        headers = {"Content-Type": "application/json"}

        # Make the API call
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                # Parse the response
                predictions = response.json().get("predictions", [])

                # Display results
                st.success("Predictions:")
                for sentence, prediction in zip(sentences, predictions):
                    st.write(f"- **Input**: {sentence}")
                    st.write(f"  **Prediction**: {prediction}")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error while calling the API: {e}")
    else:
        st.warning("Please enter at least one sentence with a `[MASK]` token.")
