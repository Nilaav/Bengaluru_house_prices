import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("Bangalore House Price Prediction")

# Inputs
bhk = st.number_input("BHK", min_value=1)
sqft = st.number_input("Total Sqft", min_value=1.0)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balcony", min_value=0)

# Predict
if st.button("Predict"):
    input_dict = {
        'bhk': bhk,
        'total_sqft': sqft,
        'bath': bath,
        'balcony': balcony
    }

    input_df = pd.DataFrame([input_dict])

    # Match model columns
    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]}")