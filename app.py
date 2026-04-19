if st.button("Predict"):
    input_dict = {
        'bhk': bhk,
        'total_sqft': sqft,
        'bath': bath,
        'balcony': balcony
    }

    input_df = pd.DataFrame([input_dict])

    # Add missing columns (VERY IMPORTANT)
    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match model
    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]}")