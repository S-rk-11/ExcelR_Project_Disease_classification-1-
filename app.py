import streamlit as st
import pickle

# Load the saved pipeline
with open('disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.set_page_config(page_title="Drug Condition Predictor", layout="centered")
st.title("Drug Condition Predictor")

# User input
user_input = st.text_area("Enter the patient's drug review here:")

if st.button("Predict Condition"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"Predicted Medical Condition: **{prediction}**")
