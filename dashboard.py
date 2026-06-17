import streamlit as st
import requests

st.title("SahiCheck AI Dashboard")
st.write("Fake News + Phishing + Fraud Detection System")

user_input = st.text_area("Enter text or URL")

if st.button("Predict"):
    if user_input:

        # Dummy response (works even if API not connected)
        st.success("Prediction: SAFE / FAKE / PHISHING / FRAUD")
        st.info("Confidence: 88%")

        # OPTIONAL: if your FastAPI is running
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": user_input}
            )
            st.json(response.json())
        except:
            st.warning("API not connected (showing demo output)")

    else:
        st.error("Please enter input")