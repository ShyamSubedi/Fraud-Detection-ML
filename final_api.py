
import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

# Initialize FastAPI app
app = FastAPI()

# Get the current working directory (for Render or local)
BASE_DIR = os.getcwd()

# Correct model path
model_path = os.path.join(BASE_DIR, "fraud_detection_xgboost.pkl")

# Try loading the model with error handling
try:
    print(f"✅ Loading model from: {model_path}")  # Debugging log
    model = joblib.load(model_path)  
    print("✅ Model Loaded Successfully!")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Model loading failed: {str(e)}")

@app.get("/")
def root():
    return {"message": "🚀 Fraud Detection API is running with the latest path changes!"}

@app.post("/predict")
def predict_fraud(transaction: dict):
    try:
        df = pd.DataFrame([transaction])  # Convert input JSON to DataFrame

        # Match model features
        expected_features = ['amount', 'isFlaggedFraud', 'transaction_difference', 'isMerchant', 'amount_ratio', 'type_encoded']
        df = df[expected_features]  # Drop unexpected columns

        prediction = model.predict(df)  # Get prediction
        return {"isFraud": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    