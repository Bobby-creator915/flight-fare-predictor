import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Flight Fare Predictor",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Flight Fare Prediction System")
st.markdown("### Plan your trip and get an AI-powered fare prediction")
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

    airline = st.selectbox(
        "✈️ Airline",
        list(airline_map.keys())
    )

    source = st.selectbox(
        "📍 Source",
        list(source_map.keys())
    )

    total_stops = st.number_input(
        "🔁 Total Stops",
        min_value=0,
        max_value=5,
        value=0
    )


with col2:

    destination = st.selectbox(
        "🏁 Destination",
        list(destination_map.keys())
    )

    journey_day = st.number_input(
        "📅 Journey Day",
        min_value=1,
        max_value=31,
        value=15
    )

    journey_month = st.number_input(
        "📆 Journey Month",
        min_value=1,
        max_value=12,
        value=6
    )


with col3:

    dep_hour = st.number_input(
        "🛫 Departure Hour",
        min_value=0,
        max_value=23,
        value=10
    )

    dep_min = st.number_input(
        "🛫 Departure Minute",
        min_value=0,
        max_value=59,
        value=30
    )

    arrival_hour = st.number_input(
        "🛬 Arrival Hour",
        min_value=0,
        max_value=23,
        value=13
    )

    arrival_min = st.number_input(
        "🛬 Arrival Minute",
        min_value=0,
        max_value=59,
        value=45
    )


st.divider()


# ---------------- PREDICTION ----------------

if st.button("💰 Predict Fare", use_container_width=True):

    data = {
        "Airline": airline_map[airline],
        "Source": source_map[source],
        "Destination": destination_map[destination],
        "Total_Stops": total_stops,
        "Journey_Day": journey_day,
        "Journey_Month": journey_month,
        "Dep_Hour": dep_hour,
        "Dep_Min": dep_min,
        "Arrival_Hour": arrival_hour,
        "Arrival_Min": arrival_min
    }

    with st.spinner("🔍 Calculating fare..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data,
                timeout=30
            )

            if response.status_code == 200:

                result = response.json()

                prediction = result["predicted_fare"]

                st.success("✅ Prediction Completed Successfully!")

                st.markdown("---")

                st.subheader("💰 Estimated Flight Fare")

                st.metric(
                    label="Predicted Fare",
                    value=f"₹ {prediction:,.2f}"
                )

            else:

                st.error(
                    f"❌ API Error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Unable to connect to the FastAPI backend. "
                "Make sure FastAPI is running on port 8000."
            )

        except requests.exceptions.RequestException as e:

            st.error(
                f"❌ Request failed: {e}"
            )