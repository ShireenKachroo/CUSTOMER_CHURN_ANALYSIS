from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

# -----------------------------
# App initialization
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Load ML pipeline
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_pipeline.pkl")

pipeline = joblib.load(MODEL_PATH)

# -----------------------------
# Home page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    # Collect form data
    data = {
        "tenure": int(request.form["tenure"]),
        "MonthlyCharges": float(request.form["MonthlyCharges"]),
        "TotalCharges": float(request.form["TotalCharges"]),
        "gender": request.form["gender"],
        "SeniorCitizen": int(request.form["SeniorCitizen"]),
        "Partner": request.form["Partner"],
        "Dependents": request.form["Dependents"],
        "PhoneService": request.form["PhoneService"],
        "InternetService": request.form["InternetService"],
        "Contract": request.form["Contract"],
        "PaymentMethod": request.form["PaymentMethod"]
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # Predict
    prediction = pipeline.predict(input_df)[0]
    probability = pipeline.predict_proba(input_df)[0][1]

    result = "Churn" if prediction == 1 else "No Churn"

    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability, 2)
    )

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
