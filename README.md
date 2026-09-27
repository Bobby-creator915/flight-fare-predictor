# ✈️ Flight Fare Prediction System

A complete end-to-end Machine Learning web application that predicts flight ticket prices based on flight details.

The system uses a trained **Random Forest Regressor** model, a **FastAPI backend** for serving predictions, and a **Streamlit frontend** for the user interface.

## 🚀 Live Demo

[Open Flight Fare Predictor](https://flight-fare-predictor-thvjl2chm6wnswz6ryx3db.streamlit.app/)

---

## 🎯 Project Objective

The objective of this project is to build a Machine Learning system that can estimate flight ticket prices based on information such as airline, source, destination, number of stops, journey date, departure time, and arrival time.

---

## ⚙️ How the System Works

```text
User
 │
 ▼
Streamlit Frontend
 │
 │ HTTP Request
 ▼
FastAPI Backend
 │
 ▼
Machine Learning Model
 │
 ▼
Predicted Flight Fare
```

The Streamlit application collects the user's flight details and sends them to the FastAPI `/predict` endpoint.

The FastAPI backend processes the request and uses the trained Machine Learning model to generate the predicted fare.

---

## ✨ Features

* ✈️ Flight fare prediction
* 🤖 Machine Learning-based prediction
* 🌐 Streamlit web interface
* ⚡ FastAPI prediction backend
* 🐳 Docker configuration
* 🔌 REST API endpoint
* 💰 Fare displayed in Indian Rupees
* 📊 User-friendly input interface
* ☁️ Cloud deployment

---

## 🤖 Machine Learning

The project uses regression algorithms to predict the numerical flight fare.

Models explored during development include:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* CatBoost Regressor

The final application uses the selected **Random Forest Regressor** model.

The trained model is saved as:

```text
flight_fare_model.pkl
```

---

## 📊 Input Features

The model uses the following features:

| Feature          | Description                  |
| ---------------- | ---------------------------- |
| Airline          | Airline operating the flight |
| Source           | Departure city               |
| Destination      | Arrival city                 |
| Total Stops      | Number of stops              |
| Journey Day      | Day of journey               |
| Journey Month    | Month of journey             |
| Departure Hour   | Departure hour               |
| Departure Minute | Departure minute             |
| Arrival Hour     | Arrival hour                 |
| Arrival Minute   | Arrival minute               |

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* FastAPI
* Uvicorn
* Docker
* GitHub
* Render

---

## 📁 Project Structure

```text
flight-fare-predictor/
│
├── .github/
│   └── workflows/
│
├── images/
│   ├── home_page.png
│   └── prediction_result.png
│
├── app.py
├── api.py
├── flight_fare_model.pkl
├── requirements.txt
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── flight_fare_predicition_model_datamites (1).ipynb
└── README.md
```

---

## 🔌 API

The FastAPI backend provides the following endpoints:

### Health Check

```text
GET /
```

Returns:

```json
{
  "message": "Flight Fare Prediction API is running"
}
```

### Prediction

```text
POST /predict
```

The `/predict` endpoint receives flight details and returns the predicted fare.

---

## ☁️ Deployment

The application uses a two-service deployment architecture.

### Frontend

The Streamlit frontend is deployed using **Streamlit Community Cloud**.

### Backend

The FastAPI backend is deployed using **Render**.

### Deployment Flow

```text
GitHub
  │
  ├──────────────► Streamlit Cloud
  │                    │
  │                    ▼
  │              Streamlit Frontend
  │                    │
  │                    ▼
  │              FastAPI Backend
  │                    │
  └──────────────► Render
                       │
                       ▼
                Machine Learning Model
```

---

## 🖼️ Screenshots

### Home Page

https://github.com/Bobby-creator915/flight-fare-predictor/blob/main/images/home_page.png?raw=true

### Prediction Result

https://github.com/Bobby-creator915/flight-fare-predictor/blob/main/images/prediction_result.png?raw=true

---

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/Bobby-creator915/flight-fare-predictor.git
cd flight-fare-predictor
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Run the FastAPI backend

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Run the Streamlit frontend

In another terminal:

```bash
streamlit run app.py
```

The Streamlit application will connect to the FastAPI backend running on port `8000`.

---

## 👨‍💻 Author

**Bobby**

GitHub: [Bobby-creator915](https://github.com/Bobby-creator915)

