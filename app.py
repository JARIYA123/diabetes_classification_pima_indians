from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

# Load model and scaler
model = joblib.load("models/pima_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.post("/predict")
def predict(data: dict):
    # Convert input JSON to dataframe
    df = pd.DataFrame([data])
    
    # Scale features
    df_scaled = scaler.transform(df)
    
    # Predict
    prediction = model.predict(df_scaled)
    
    return {"Diabetes": int(prediction[0])}