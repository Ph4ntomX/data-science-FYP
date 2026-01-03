import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# // Load trained model
model = joblib.load("heat_control_predictor.joblib")
scaler = joblib.load("scaler.joblib")

# // Page Config
st.set_page_config(
    page_title="Heat Control Predictor",
    layout="centered"
)

st.title("🌆 Heat Control Predictor")
st.markdown("""
This tool simulates how **urban environmental factors** influence  
**heat-related health risks**, supporting **SDG 13 (Climate Action)**  
and **SDG 15 (Life on Land)**.
""")

# // Preset City Configurations
city_presets = {
    "Custom": None,
    "Kuala Lumpur (Tropical Urban)": {
        "Temperature": 32,
        "Population Density": 7000,
        "Energy Consumption": 5084,
        "AQI": 75,
        "Greenness": 35,
        "Wind": 8,
        "Humidity": 78,
        "Rainfall": 2400,
        "Land Cover": "Urban"
    },
    "Singapore (Dense & Tropical)": {
        "Temperature": 31,
        "Population Density": 8000,
        "Energy Consumption": 5016,
        "AQI": 55,
        "Greenness": 47,
        "Wind": 12,
        "Humidity": 80,
        "Rainfall": 2400,
        "Land Cover": "Urban"
    },
    "Jakarta (High Risk)": {
        "Temperature": 33,
        "Population Density": 11000,
        "Energy Consumption": 3800,
        "AQI": 95,
        "Greenness": 25,
        "Wind": 8,
        "Humidity": 75,
        "Rainfall": 1800,
        "Land Cover": "Industrial"
    },
    "Tokyo (Mixed Urban)": {
        "Temperature": 29,
        "Population Density": 6500,
        "Energy Consumption": 5200,
        "AQI": 60,
        "Greenness": 35,
        "Wind": 10,
        "Humidity": 70,
        "Rainfall": 1500,
        "Land Cover": "Urban"
    }
}

# // Sidebar Inputs
st.sidebar.header("🏙️ City Configuration")

selected_city = st.sidebar.selectbox("Choose a preset city", city_presets.keys())
st.sidebar.caption("Customize inputs or use preset configurations for common cities. The data used for presets is purely mock and may not reflect real-world conditions.")

preset = city_presets[selected_city]

def preset_value(key, default):
    return preset[key] if preset else default

temperature = st.sidebar.slider("Temperature (°C)", 20, 40, preset_value("Temperature", 30))
population_density = st.sidebar.slider("Population Density (people/km²)", 500, 15000, preset_value("Population Density", 5000))
energy = st.sidebar.slider("Energy Consumption (kWh)", 1000, 8000, preset_value("Energy Consumption", 3000))
aqi = st.sidebar.slider("Air Quality Index (AQI)", 0, 200, preset_value("AQI", 60))
greenness = st.sidebar.slider("Urban Greenness Ratio (%)", 1, 100, preset_value("Greenness", 40))
wind = st.sidebar.slider("Wind Speed (km/h)", 0, 30, preset_value("Wind", 10))
humidity = st.sidebar.slider("Humidity (%)", 20, 100, preset_value("Humidity", 70))
rainfall = st.sidebar.slider("Annual Rainfall (mm)", 0, 4000, preset_value("Rainfall", 1500))
land_cover = st.sidebar.selectbox(
    "Land Cover Type",
    ["Urban", "Industrial", "Green Space", "Water"],
    index=["Urban", "Industrial", "Green Space", "Water"].index(preset_value("Land Cover", "Urban"))
)

# // Encode Inputs

input_data = pd.DataFrame([{
    "Temperature (°C)": temperature,
    "Population Density (people/km²)": population_density,
    "Energy Consumption (kWh)": energy,
    "Air Quality Index (AQI)": aqi,
    "Urban Greenness Ratio (%)": greenness,
    "Wind Speed (km/h)": wind,
    "Humidity (%)": humidity,
    "Annual Rainfall (mm)": rainfall,
    "Land Cover_Green Space": 1 if land_cover == "Green Space" else 0,
    "Land Cover_Industrial": 1 if land_cover == "Industrial" else 0,
    "Land Cover_Urban": 1 if land_cover == "Urban" else 0,
    "Land Cover_Water": 1 if land_cover == "Water" else 0
}])

# // Create Features

input_data['Heat Stress Index'] = input_data['Humidity (%)'] * input_data['Temperature (°C)']
input_data['Urban Pressure Index'] = input_data['Population Density (people/km²)'] / input_data['Urban Greenness Ratio (%)']
input_data['Cooling Potential'] = input_data['Wind Speed (km/h)'] + input_data['Urban Greenness Ratio (%)'] + input_data['Annual Rainfall (mm)']

# // Scale Inputs

num_columns = ['Population Density (people/km²)', 'Energy Consumption (kWh)', 'Air Quality Index (AQI)', 'Annual Rainfall (mm)', 'Heat Stress Index', 'Urban Pressure Index', 'Cooling Potential']
input_data[num_columns] = scaler.transform(input_data[num_columns])

# // Prediction
if st.button("🔍 Predict Heat-Related Health Impact"):
    prediction = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")
    st.metric("Predicted Heat Mortality Rate (per 100k)", f"{prediction:.2f}")

    # // Risk Thresholds
    if prediction < 20:
        st.success("🟢 Low Risk — City conditions are relatively safe.")
    elif prediction < 35:
        st.warning("🟡 Moderate Risk — Urban heat mitigation recommended.")
    else:
        st.error("🔴 High Risk — Immediate urban cooling actions needed.")