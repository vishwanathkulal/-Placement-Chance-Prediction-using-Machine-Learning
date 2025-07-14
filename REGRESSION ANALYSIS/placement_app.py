import streamlit as st
import pandas as pd
import joblib

# Load the model and feature names
model = joblib.load("placement_predictor_regression.pkl")
feature_names = joblib.load("placement_features.pkl")

st.set_page_config(page_title="Placement Chance Predictor", layout="centered")

st.title("🎓 Placement Chance Predictor")
st.markdown("Enter your academic and skill details below to estimate your placement chance.")

# Create input fields dynamically based on feature names
input_data = {}

for feature in feature_names:
    if feature in ['CGPA']:
        input_data[feature] = st.slider(f"{feature} (0 - 10)", 0.0, 10.0, 7.0)
    elif feature in ['AptitudeScore', 'MockTestScore']:
        input_data[feature] = st.slider(f"{feature} (0 - 100)", 0, 100, 70)
    elif feature in ['ProgrammingSkill', 'CommunicationSkill']:
        input_data[feature] = st.selectbox(f"{feature} (1: Poor, 5: Excellent)", [1, 2, 3, 4, 5])
    else:
        input_data[feature] = st.number_input(f"{feature}", min_value=0, max_value=10, value=1)

# Predict on button click
if st.button("Predict Placement Chance"):
    input_df = pd.DataFrame([input_data])
    input_df = input_df[feature_names]  # Ensure correct column order
    prediction = model.predict(input_df)[0]

    st.success(f"🎯 Your predicted placement chance is: **{prediction:.2f}**")

    if prediction >= 0.75:
        st.balloons()
        st.markdown("👍 **Great! You have a high chance of placement.**")
    elif prediction >= 0.5:
        st.markdown("🙂 **Fair chance. Consider improving skills to boost confidence.**")
    else:
        st.markdown("⚠️ **Low chance. Focus on building skills and mock tests.**")
