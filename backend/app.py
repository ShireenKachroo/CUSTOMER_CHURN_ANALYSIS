from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load model & scaler
model = joblib.load("../models/logistic_regression.pkl")
scaler = joblib.load("../models/scaler.pkl")

# EXACT feature list from training
FEATURE_COLUMNS = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
    'gender_Male', 'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes',
    'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No internet service', 'TechSupport_Yes',
    'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',
    'Contract_One year', 'Contract_Two year',
    'PaperlessBilling_Yes',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    form = request.form

    # 1. Create empty input frame
    input_df = pd.DataFrame(
        np.zeros((1, len(FEATURE_COLUMNS))),
        columns=FEATURE_COLUMNS
    )

    # 2. Numerical features
    input_df["SeniorCitizen"] = int(form["SeniorCitizen"])
    input_df["tenure"] = int(form["tenure"])
    input_df["MonthlyCharges"] = float(form["MonthlyCharges"])
    input_df["TotalCharges"] = float(form["TotalCharges"])

    # 3. Binary categorical
    if form["gender"] == "Male":
        input_df["gender_Male"] = 1

    if form["Partner"] == "Yes":
        input_df["Partner_Yes"] = 1

    if form["Dependents"] == "Yes":
        input_df["Dependents_Yes"] = 1

    if form["PhoneService"] == "Yes":
        input_df["PhoneService_Yes"] = 1
        input_df["MultipleLines_Yes"] = 1
    else:
        input_df["MultipleLines_No phone service"] = 1

    # 4. Internet related logic
    if form["InternetService"] == "No":
        input_df["InternetService_No"] = 1

        for col in [
            "OnlineSecurity_No internet service",
            "OnlineBackup_No internet service",
            "DeviceProtection_No internet service",
            "TechSupport_No internet service",
            "StreamingTV_No internet service",
            "StreamingMovies_No internet service"
        ]:
            input_df[col] = 1

    else:
        if form["InternetService"] == "Fiber optic":
            input_df["InternetService_Fiber optic"] = 1

        input_df["OnlineSecurity_Yes"] = 1
        input_df["OnlineBackup_Yes"] = 1
        input_df["DeviceProtection_Yes"] = 1
        input_df["TechSupport_Yes"] = 1
        input_df["StreamingTV_Yes"] = 1
        input_df["StreamingMovies_Yes"] = 1

    # 5. Contract
    contract_col = f"Contract_{form['Contract']}"
    if contract_col in input_df.columns:
        input_df[contract_col] = 1

    # 6. Paperless billing (assume Yes)
    input_df["PaperlessBilling_Yes"] = 1

    # 7. Payment method
    payment_col = f"PaymentMethod_{form['PaymentMethod']}"
    if payment_col in input_df.columns:
        input_df[payment_col] = 1

    # 8. Scale & predict
    X_scaled = scaler.transform(input_df)
    pred = model.predict(X_scaled)[0]
    prob = model.predict_proba(X_scaled)[0][1]

    result = "Churn" if pred == 1 else "No Churn"

    return render_template(
        "index.html",
        prediction=result,
        probability=f"{prob * 100:.2f}%"
    )

if __name__ == "__main__":
    app.run(debug=True)
