from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Flight Fare Prediction API",
    description="API for predicting flight fares using a trained machine learning model.",
    version="1.0.0"
)

# Load trained model
model = joblib.load("flight_fare_model.pkl")


@app.get("/")
def home():
    return {
        "message": "Flight Fare Prediction API is running"
    }


@app.post("/predict")
def predict_fare(data: dict):

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_fare": round(float(prediction), 2)
    }