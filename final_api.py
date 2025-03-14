from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

app = FastAPI()

# Try loading the model with error handling
try:
    model = joblib.load("/kaggle/working/fraud_detection_xgboost.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Model loading failed: {str(e)}")

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
