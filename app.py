import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("flight_fare_model.pkl")

st.set_page_config(page_title="Flight Fare Predictor", layout="wide")

st.title("✈️ Flight Fare Prediction System")
st.markdown("Plan your trip and get instant fare predictions using AI")
st.divider()

# ---------------- MAPPINGS ----------------
airline_map = {
    "IndiGo": 3,
    "Air India": 1,
    "SpiceJet": 4,
    "Vistara": 2
}

source_map = {
    "Delhi": 0,
    "Mumbai": 3,
    "Bangalore": 2,
    "Chennai": 1
}

destination_map = {
    "Delhi": 0,
    "Mumbai": 3,
    "Bangalore": 2,
    "Chennai": 1
}

# ---------------- INPUT SECTION ----------------
st.subheader("📍 Enter Travel Details")

col1, col2, col3 = st.columns(3)

with col1:
    airline = st.selectbox("✈️ Airline", list(airline_map.keys()))
    source = st.selectbox("📍 Source", list(source_map.keys()))
    total_stops = st.number_input("🔁 Total Stops", 0, 5)

with col2:
    destination = st.selectbox("🏁 Destination", list(destination_map.keys()))
    journey_day = st.number_input("📅 Journey Day", 1, 31)
    journey_month = st.number_input("📆 Journey Month", 1, 12)

with col3:
    dep_hour = st.number_input("🛫 Departure Hour", 0, 23)
    dep_min = st.number_input("🛫 Departure Minute", 0, 59)
    arrival_hour = st.number_input("🛬 Arrival Hour", 0, 23)
    arrival_min = st.number_input("🛬 Arrival Minute", 0, 59)

# ---------------- PREDICT BUTTON ----------------
if st.button("💰 Predict Fare"):

    with st.spinner("🔍 Calculating best fare for your trip..."):

        input_data = pd.DataFrame([[
            airline_map[airline],
            source_map[source],
            destination_map[destination],
            total_stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min
        ]], columns=[
            'Airline',
            'Source',
            'Destination',
            'Total_Stops',
            'Journey_Day',
            'Journey_Month',
            'Dep_Hour',
            'Dep_Min',
            'Arrival_Hour',
            'Arrival_Min'
        ])

        prediction = model.predict(input_data)[0]

    st.success("✅ Prediction Completed Successfully!")

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            background-color:#0f172a;
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0px 0px 10px rgba(0,0,0,0.3);
        ">
            <h2 style="color:#00ffcc;">💰 Estimated Flight Fare</h2>
            <h1 style="color:#ffffff;">₹ {prediction:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    



    



