import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Required for first-time use
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

# Text Preprocessing
stop_words = set(stopwords.words('english'))
lemma = WordNetLemmatizer()

def clean_text(text):
    text = re.sub('[^a-zA-Z:]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [lemma.lemmatize(w) for w in words if w not in stop_words]
    return ' '.join(words)

# Load pipeline
with open('disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.set_page_config(page_title="Drug Condition Predictor", layout="centered")
st.title("Drug Condition Predictor")

user_input = st.text_area("Enter the patient's drug review here:")

if st.button("Predict Condition"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"Predicted Medical Condition: **{prediction}**")
