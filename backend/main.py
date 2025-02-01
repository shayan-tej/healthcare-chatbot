from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace "*" with your frontend URL in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Change working directory (if needed)
os.chdir(f'{os.getcwd()}/backend')

# Load training data
training = pd.read_csv('./Data/Training.csv')
cols = training.columns[:-1]
x = training[cols]
y = training['prognosis']

# Preprocess data
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

# Train Decision Tree model
clf = DecisionTreeClassifier()
clf.fit(x, y)

# Create a mapping from symptom names to column indices
symptoms_dict = {symptom: idx for idx, symptom in enumerate(cols)}

# Define Pydantic models for request and response
class SymptomRequest(BaseModel):
    symptoms: List[str]
    days: int

class PredictionResponse(BaseModel):
    disease: str
    description: str
    precautions: List[str]
    severity_advice: str

# Helper function to convert symptoms to binary vector
def symptoms_to_binary(symptoms):
    binary_vector = np.zeros(len(cols))
    for symptom in symptoms:
        if symptom in symptoms_dict:
            binary_vector[symptoms_dict[symptom]] = 1
    return binary_vector

# FastAPI endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict_disease(request: SymptomRequest):
    symptoms_exp = request.symptoms
    days = request.days

    # Convert symptoms to binary vector
    input_vector = symptoms_to_binary(symptoms_exp)

    # Predict disease
    primary_prediction = clf.predict([input_vector])
    disease = le.inverse_transform(primary_prediction)[0]

    # Add logic for description, precautions, and severity advice
    description = "Sample description for " + disease  # Replace with actual logic
    precautions = ["Precaution 1", "Precaution 2", "Precaution 3"]  # Replace with actual logic
    severity_advice = "Sample severity advice for " + disease  # Replace with actual logic

    return {
        "disease": disease,
        "description": description,
        "precautions": precautions,
        "severity_advice": severity_advice
    }

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)