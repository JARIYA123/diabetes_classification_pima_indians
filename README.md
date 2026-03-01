# Pima Diabetes Prediction API 🩺

## Overview

This project predicts whether a patient has diabetes using the **Pima Indians Diabetes Dataset**.  
The ML model is trained and evaluated in Python, then deployed as a **FastAPI REST API** for real-time predictions.
This project demonstrates an **end-to-end workflow**:
- Data exploration and visualization
- Data preprocessing & feature engineering
- Model training and evaluation
- Model saving
- Deployment with FastAPI
---

## Project Structure

project2/
├── data/
│ └── diabetes.csv
├── models/
│ ├── pima_model.pkl
│ └── scaler.pkl
├── notebooks/
│ └── pima_diabetes.ipynb
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ └── predict.py
├── images/ 
├── app.py
├── requirements.txt
└── README.md
............................................................
## Data Exploration

- Check dataset info, null values, and statistics
- Visualize distributions
---
## Model Training & Evaluation

- Model used: **Logistic Regression**
-  Train/Test split: 80/20
- Metrics: Accuracy, Confusion Matrix, Classification Report
Example results:
-----------------------------------------------------------------------------
Accuracy: 0.78
Confusion Matrix:
[[90 12]
[25 36]]
Classification Report:
precision recall f1-score support
0 0.78 0.88 0.82 102
1 0.75 0.59 0.66 61
--------------------------------------------------------------------  
## Model Deployment (FastAPI)

Run the API:
```bash
uvicorn app:app --reload
`````
Example API Request
POST request to /predict:
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 79,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 33
}
Response:
{
  "Diabetes": 0
}
## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib
* Matplotlib & Seaborn
---------------------------------------------------------------------------
## Future Improvements

- Use more advanced ML models (XGBoost, RandomForest)
- Add web frontend for user-friendly input
- Dockerize the API
- Deploy to cloud platforms (AWS, Render, or Railway)
## Author

Jariya – Machine Learning enthusiast building real-world ML projects .
