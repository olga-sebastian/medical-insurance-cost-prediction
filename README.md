# medical-insurance-cost-prediction
This project develops a machine learning model to predict medical insurance costs based on factors such as age, BMI, number of children, smoking status, and region. The model is trained using a Random Forest Regressor, with Linear Regression used as a baseline for performance comparison. The final model is deployed using Streamlit for interactive predictions.

Project Overview
Goal: Predict individual medical insurance costs using supervised machine learning.
Dataset: Two Kaggle datasets were merged to improve prediction accuracy.
Models Used:
Baseline: Linear Regression
Final Model: Random Forest Regressor (optimized for accuracy)
Deployment: Streamlit web app (app.py) to allow users to input their details and receive predictions.
Files in This Repository
This repository contains all necessary code, datasets, and the trained model.

Code & Deployment
app.py – Streamlit web app for medical insurance cost prediction.
medical_insurance_cost_prediction.ipynb – Jupyter Notebook with data exploration, preprocessing, feature engineering, model training, and evaluation.
Datasets
We used two Kaggle datasets and merged them to improve prediction precision:
insurance.csv – One of the original Kaggle datasets.
Medical_insurance.csv – Second Kaggle dataset used for merging.
merged_medical_insurance.csv – Merged dataset combining both Kaggle datasets for increased accuracy.
processed_medical_insurance.csv – Final cleaned dataset used for model training.

Trained Model
insurance_cost_model.pkl – Serialized Random Forest model saved using joblib.

How the Prediction Model Works

User Inputs:
Age, BMI, Number of Children
Smoker status (Yes/No)
Region (Northwest, Northeast, Southeast, Southwest)

Feature Engineering:
One-hot encoding for categorical variables.
BMI categories (Underweight, Normal, Overweight, Obese).
Interaction feature for high BMI and smoking.

Models Used:
Linear Regression – Used as a baseline model.
Random Forest Regressor – Final model chosen for its superior accuracy.
Prediction Output:

The trained Random Forest model predicts the insurance cost.
The Streamlit app displays the estimated cost.
