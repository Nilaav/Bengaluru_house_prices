import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Bangalore House Price Prediction")

# Inputs
bhk = st.number_input("BHK", min_value=1)
sqft = st.number_input("Total Sqft", min_value=1.0)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balcony", min_value=0)

# Predict
if st.button("Predict"):
    if sqft <= 0:
        st.error("Sqft must be positive")
    else:
        input_df = pd.DataFrame([[bhk, sqft, bath, balcony]],
                                columns=['bhk','total_sqft','bath','balcony'])

        model_columns = model.feature_names_in_
        input_df = input_df.reindex(columns=model_columns, fill_value=0)

        prediction = model.predict(input_df)
        st.success(f"Predicted Price: {prediction[0]}")