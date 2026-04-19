import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Bangalore House Price Prediction")

bhk = st.number_input("BHK", min_value=1)
sqft = st.number_input("Total Sqft", min_value=1.0)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balcony", min_value=0)

if st.button("Predict"):
    input_df = pd.DataFrame([[bhk, sqft, bath, balcony]],
                            columns=['bhk', 'total_sqft', 'bath', 'balcony'])

    prediction = model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]}")