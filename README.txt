📌 Fraud Detection API

🚀 Overview

This is a Fraud Detection API built using FastAPI and deployed on Render. The API predicts whether a financial transaction is fraudulent based on various features using an XGBoost Machine Learning model.

📂 Project Structure

fraud-detection-api/
│── app.py                     # FastAPI application
│── fraud_detection_xgboost.pkl # Trained XGBoost model
│── requirements.txt            # Python dependencies
│── README.md                   # Project documentation

🛠 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/fraud-detection-api.git
cd fraud-detection-api

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the API Locally

uvicorn app:app --host 0.0.0.0 --port 8000

🎯 API Endpoints

Endpoint

Method

Description

/predict

POST

Predicts whether a transaction is fraudulent

📝 Example Request (JSON Payload)

{
  "amount": 5000,
  "isFlaggedFraud": 0,
  "transaction_difference": 1000,
  "isMerchant": 0,
  "amount_ratio": 0.5,
  "type_encoded": 1
}

✅ Example Response

{
  "isFraud": 1  # 1 = Fraudulent, 0 = Not Fraudulent
}

🚀 Deployment on Render

Push all files to GitHub.

Sign up on Render.

Create a New Web Service.

Connect your GitHub repo.

Use this Start Command:

uvicorn app:app --host 0.0.0.0 --port 8000

Click Deploy.

🔥 Testing the Live API

Once deployed, use the Render URL (e.g., https://your-app.onrender.com/predict) to send requests:

import requests

url = "https://your-app.onrender.com/predict"  # Replace with your Render URL

data = {
    "amount": 5000,
    "isFlaggedFraud": 0,
    "transaction_difference": 1000,
    "isMerchant": 0,
    "amount_ratio": 0.5,
    "type_encoded": 1
}

response = requests.post(url, json=data)
print(response.status_code, response.json())

🛠 Future Improvements

✅ Enhance feature engineering

✅ Add logging & monitoring

✅ Improve model with new fraud patterns

📜 License

This project is open-source under the MIT License.

💡 Developed for learning and research purposes! 🚀

