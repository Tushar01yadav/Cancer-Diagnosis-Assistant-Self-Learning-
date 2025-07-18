import streamlit as st
import numpy as np
import pickle

# Load trained model
with open('rfe_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🩺 Cancer Diagnosis Assistant")
st.write("Enter patient data to predict whether the tumor is benign or malignant.")

# Input features (selecting a few for simplicity)
mean_radius = st.slider("Mean Radius", 5.0, 30.0, 14.0)
mean_texture = st.slider("Concavity Mean ", 10.0, 40.0, 20.0)
mean_perimeter = st.slider("concavity worst", 40.0, 200.0, 85.0)
mean_area = st.slider("radius_se", 100.0, 2500.0, 500.0)
mean_smoothnes = st.slider("compactness_worst", 0.05, 0.2, 0.1)
mean_smoothns = st.slider("compactness_mean", 0.05, 0.2, 0.1)
mean_smoothess = st.slider("smoothness_worst", 0.05, 0.2, 0.1)

# Prepare input
input_data = np.array([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "Malignant" if prediction[0] == 0 else "Benign"
    st.success(f"The tumor is likely: **{result}**")
