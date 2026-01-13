# Customer Churn Prediction System

An **end-to-end Machine Learning project** that predicts customer churn using structured customer data.
The project covers the **complete ML lifecycle** — from data preprocessing and feature engineering to model training, evaluation, and deployment with a Flask-based web interface.

---

## Project Overview

Customer churn is a critical business problem where companies want to identify customers who are likely to stop using their service.
This project builds a **binary classification system** that predicts whether a customer will churn based on demographic, service usage, and billing-related features.

The final model is deployed using **Flask**, allowing users to input customer details through a web UI and receive real-time churn predictions.

---

## Key Features

* End-to-end ML pipeline (data → model → deployment)
* Logistic Regression model with feature scaling
* Manual feature engineering & one-hot encoding
* Model evaluation using accuracy, precision, recall, F1-score
* Flask-based web application for real-time inference
* Clean separation of backend, models, and UI templates
* Free-tier deployment (cold start enabled)

---

## Tech Stack

### **Programming & ML**

* Python
* Pandas, NumPy
* Scikit-learn

### **Modeling**

* Logistic Regression
* StandardScaler
* GridSearchCV (hyperparameter tuning)

### **Backend & Deployment**

* Flask
* HTML (Jinja2 Templates)
* Render (free-tier hosting)

---

## Project Structure

```

customer_churn_project/
│
├── backend/
│   ├── app.py				    # Flask application
|   |── requirements.txt
│   └── templates/
│       └── index.html          # Web UI
│
|── data/
│   ├── processed_data.csv		# Flask application
|   |── raw.csv
|
├── models/
│   ├── churn_pipeline.pkl		# Trained ML Pipeline
|   ├──  logistic_regression.pkl
|   ├──  scaler.pkl
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── preprocessing.ipynb
│   └── train_model.ipynb
|
|── sql/
│   ├── create_tables.sql
│   ├── queries.sql
│
├── gitignore
└── README.md

````

---

## Model Details

* **Algorithm:** Logistic Regression
* **Why Logistic Regression?**
  * Interpretable coefficients
  * Strong baseline for binary classification
  * Widely used in industry churn models

### **Evaluation Metrics (Test Set)**

* Accuracy: ~80%
* Recall (Churn class): ~53%
* Precision (Churn class): ~65%
* F1-score: ~58%

> Class imbalance was handled using stratified splitting and metric-based evaluation.

---

## How to Run Locally

### Clone the repository

```bash
git clone https://github.com/ShireenKachroo/customer-churn-prediction.git
cd customer-churn-prediction
````

### Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask app

```bash
cd backend
python app.py
```

### Open in browser
https://customer-churn-predictor-oeol.onrender.com/

## Deployment Note

This project is deployed on **Render (free tier)**.

> ⚠️ Free-tier instances may spin down after inactivity, causing a **cold start delay of ~30–50 seconds** on first request.
> This is expected behavior and can be avoided in production using paid instances or container orchestration.

---

## Business Insights

* Customers on **month-to-month contracts** have higher churn risk
* **Fiber optic users** show higher churn probability
* **Electronic check payments** correlate with increased churn
* Longer tenure significantly reduces churn likelihood

These insights can help businesses:

* Design better retention strategies
* Offer targeted plans for high-risk users
* Improve customer lifetime value

---

## Future Improvements

* Try non-linear models (Random Forest, XGBoost)
* Add probability-based threshold tuning
* Improve UI with better styling and validation
* Integrate database logging for predictions
* Add authentication and user tracking

---

## Author

**Shireen Kachroo**

⭐ If you found this project helpful, feel free to star the repository!

