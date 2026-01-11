from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# -------------------------------
# Initialize FastAPI app
# -------------------------------
app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict customer churn using ML pipeline",
    version="1.0"
)

# -------------------------------
# Load trained pipeline
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_pipeline.pkl")

pipeline = joblib.load(MODEL_PATH)

# -------------------------------
# Input schema (RAW FEATURES)
# Must match training data columns
# -------------------------------
class ChurnInput(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    PhoneService: str
    InternetService: str
    Contract: str
    PaymentMethod: str

# -------------------------------
# Health check (optional but useful)
# -------------------------------
@app.get("/")
def home():
    return {"status": "API is running"}

# -------------------------------
# Prediction endpoint
# -------------------------------
@app.post("/predict")
def predict_churn(data: ChurnInput):

    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make prediction
    prediction = pipeline.predict(input_df)[0]
    probability = pipeline.predict_proba(input_df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(probability, 4)
    }
