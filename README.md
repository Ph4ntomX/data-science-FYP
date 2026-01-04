# Urban Heat Mortality Predictor

## Overview
This project predicts **urban heat-related health impacts** in cities using machine learning. The goal is to provide actionable insights for city planners and public health authorities to mitigate **heat stress and mortality risks** associated with urban heat islands (UHI).

The model predicts **mortality rate per 100,000 people**.

A **Streamlit app** is provided for interactive exploration.

2 joblib files are used however they are too big to upload to GitHub. They can be found in the `notebook.ipynb` file.

---

## Problem Statement
- **The Why:** Heat-related mortality is increasing due to urban heat islands. Cities lack predictive tools to plan interventions effectively.  
- **Stakeholders:** Urban planners, public health officials, citizens in dense urban areas.  
- **Impact:** Without intervention, heat stress worsens, increasing mortality and public health burden.

---

## Data Overview
- **Source:** Kaggle / Publicly available city datasets  
- **Granularity:** One row represents a city in a single year  
- **Size:** ~500 rows × 13 columns  
- **Features:**
  - Temperature (°C)
  - Population Density (people/km²)
  - Energy Consumption (kWh/person/year)
  - Air Quality Index (AQI)
  - Urban Greenness Ratio (%)
  - Wind Speed (km/h)
  - Humidity (%)
  - Annual Rainfall (mm)
  - Land Cover (Urban, Industrial, Green Space, Water)  
- **Target Variable:** Heat-related Mortality Rate (per 100,000 people)

---

## Objectives & Key Questions
- Predict heat-related mortality based on urban and environmental factors.  
- Identify which city features (e.g., population density, greenness, energy consumption) drive risk.  
- Answer questions like:
  - Which cities are most vulnerable to heat-related mortality?  
  - How does urban greenness or energy consumption influence predicted mortality?

---

## Methodology
1. **Preprocessing & Feature Engineering**
   - Derived features: Heat Stress Index, Urban Pressure Index, Cooling Potential  
   - One-hot encoding for categorical features (Land Cover)  
   - StandardScaler applied to numeric features
2. **Exploratory Data Analysis (EDA)**
   - Correlation heatmap, distribution plots, boxplots  
   - Addressed outliers and ensured no data leakage
3. **Modeling**
   - Random Forest Regressor (tuned)  
   - Baseline Linear Regression for comparison  
   - 80/20 train-test split  
   - Metrics: MAE, MSE, RMSE, R²

---

## Results
- **Performance Metrics:**
  - MAE: 0.03
  - MSE: 0.13
  - RMSE: 0.36
  - R²: 1.00  
- **Feature Importance:** Population Density, Urban Greenness Ratio, and Energy Consumption are top drivers.  

---

## Streamlit App
- **Inputs:** Temperature, Population Density, Energy Consumption, AQI, Greenness, Wind Speed, Humidity, Rainfall, Land Cover  
- **Outputs:** Predicted mortality rate
- **Preset Cities:** Singapore, Jakarta, Kuala Lumpur (default configurations)  
- **Demo URL / QR Code:** [Insert Link Here]

---

## How to Run
```bash
# Clone repository
git clone https://github.com/yourusername/urban-heat-predictor.git
cd urban-heat-predictor

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
