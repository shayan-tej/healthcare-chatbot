import { useState } from "react";
import axios from "axios";

function App() {
  const [symptoms, setSymptoms] = useState("");
  const [days, setDays] = useState("");
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send a POST request to the FastAPI backend
      const response = await axios.post("http://127.0.0.1:8000/predict", {
        symptoms: symptoms.split(",").map((s) => s.trim()), // Convert input to array
        days: parseInt(days, 10),
      });

      // Set the prediction result
      setPrediction(response.data);
      setError("");
    } catch (err) {
      setError("An error occurred while fetching the prediction.");
      console.error(err);
    }
  };

  return (
    <div>
      <h1>Healthcare Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Symptoms (comma-separated):
            <input
              type="text"
              value={symptoms}
              onChange={(e) => setSymptoms(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Days:
            <input
              type="number"
              value={days}
              onChange={(e) => setDays(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit">Predict</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {prediction && (
        <div>
          <h2>Prediction Result</h2>
          <p>
            <strong>Disease:</strong> {prediction.disease}
          </p>
          <p>
            <strong>Description:</strong> {prediction.description}
          </p>
          <p>
            <strong>Precautions:</strong>
          </p>
          <ul>
            {prediction.precautions.map((precaution, index) => (
              <li key={index}>{precaution}</li>
            ))}
          </ul>
          <p>
            <strong>Severity Advice:</strong> {prediction.severity_advice}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
