import streamlit as st
import pickle

st.title("Student Pass/Fail Prediction App")

# Input
study_hours = st.number_input("Enter number of study hours:", min_value=0.0, step=0.5)

# Load Model
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'model.pkl' is in the same folder as this script.")
    st.stop()

# Predict Button
if st.button("Predict"):
    result = model.predict([[study_hours]])
    if result[0] == 1:
        st.success("✅ The student is likely to PASS.")
    else:
        st.error("❌ The student is likely to FAIL.")
