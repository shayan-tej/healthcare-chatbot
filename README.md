# Healthcare Chatbot - React + FastAPI

This project is a healthcare chatbot that uses a Machine Learning model to predict diseases based on user-provided symptoms. The backend is built with FastAPI (Python), and the frontend is built with React (Vite).

## Features

- **Frontend**: A React app that collects user inputs (symptoms and days) and displays the prediction result.

- **Backend**: A FastAPI server that processes the inputs using a trained Machine Learning model and returns the prediction.

- **Machine Learning**: A Decision Tree Classifier trained on a healthcare dataset to predict diseases based on symptoms.

## Prerequisites

Before you begin, ensure you have the following installed:

- Node.js (for React frontend)

- Python 3.8+ (for FastAPI backend)

- pip (Python package manager)

- Git (for cloning the repository)

## Setup Instructions

1. Clone the Repository
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/healthcare-chatbot.git
   cd healthcare-chatbot
   ```

2. Set Up the Backend
   a. Navigate to the Backend Directory

   ```bash
   cd backend
   ```

   b. Install Python Dependencies
   Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   c. Run the FastAPI Server
   Start the backend server:

   ```bash
   python app.py
   The backend will run at `http://127.0.0.1:8000`.
   ```

3. Set Up the Frontend
   a. Navigate to the Frontend Directory
   Open a new terminal window and navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

   b. Install Node.js Dependencies
   Install the required Node.js packages:

   ```bash
   npm install
   ```

   c. Run the React App
   Start the frontend development server:

   ```bash
   npm run dev
   ```

   The frontend will run at `http://localhost:5173`.

4. Test the Application
   1. Open your browser and navigate to `http://localhost:5173`.
   2. Enter symptoms (comma-separated) and the number of days.
   3. Click the "Predict" button.
   4. The prediction result will be displayed on the screen.

## Project Structure

### Backend

```text
backend/
├── app.py                  # FastAPI application
├── requirements.txt        # Python dependencies
├── Data/                   # Dataset for training the ML model
└── MasterData/             # Additional data (symptom descriptions, precautions, etc.)
```

### Frontend

```text
frontend/
├── public/                 # Static assets
├── src/
│   ├── App.jsx             # Main React component
│   ├── main.jsx            # Entry point
│   └── ...                 # Other React components and styles
├── package.json            # Node.js dependencies
└── vite.config.js          # Vite configuration
```

## Technologies Used

- **Frontend**: React, Vite, Axios

- **Backend**: FastAPI, Python

- **Machine Learning**: Scikit-learn, Decision Tree Classifier
