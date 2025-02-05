import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("insurance_cost_model.pkl")

# App title
st.title("Medical Insurance Cost Predictor")

# User input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
sex = st.selectbox("Sex", ["Female", "Male"])
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])

# Convert categorical inputs
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# BMI Category (One-hot encoded)
bmi_category_overweight = 1 if 24.9 < bmi <= 29.9 else 0
bmi_category_normal = 1 if 18.5 <= bmi <= 24.9 else 0
bmi_category_obese = 1 if bmi > 29.9 else 0

# Smoker & High BMI Interaction Feature
smoker_high_bmi = 1 if smoker_yes == 1 and bmi > 30 else 0

# Create input array for prediction
input_features = np.array([[smoker_high_bmi, age, smoker_yes, bmi, children, 
                            region_northwest, region_southeast, sex_male, 
                            region_southwest, bmi_category_overweight, 
                            bmi_category_normal, bmi_category_obese]])

# Prediction button
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_features)[0]
    st.success(f"Estimated Insurance Cost: ${prediction:,.2f}")