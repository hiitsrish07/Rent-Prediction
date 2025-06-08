import streamlit as st
import joblib

model = joblib.load("rent_model.pkl")

st.title("Pune Rent Predictor")

bhk = st.number_input("Number of BHK", min_value=1, max_value=10, step=1)
location = st.text_input("Location")

if st.button("Predict"):
    pred = model.predict([[bhk, location]])
    st.success(f"Estimated Rent: ₹{int(pred[0])}")