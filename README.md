# Digitalization-SDG
Team C project -Digitalization and Sustainable Development: AI-ML Tools for Sustainability
# Day-ahead Solar Generation Forecasting for Greece (Team C)

This repository contains the data pipelines, feature engineering, and predictive models developed by Team C for the **Digitalization & Sustainable Development: AI-ML Tools for Sustainability** course delivered by BuildSkills Academy (ERASMUS+ Grant Agreement 101104419).

## 📋 Project Overview
Solar power is inherently variable due to factors like cloud cover, seasonality, and changing daylight hours. This variability complicates grid planning and balancing. This project builds an end-to-end Machine Learning pipeline to provide a **24-hour-ahead forecast** of hourly solar electricity generation across major cities in Greece. 

Our primary goal is to leverage historical generation and local weather data to outperform a simple persistence baseline model by approximately **15–20%** in MAE and RMSE.

### 🌍 SDG Alignment
- **SDG 7:** Clean Energy
- **SDG 9:** Industry and Innovation
- **SDG 11:** Sustainable Cities and Communities
- **SDG 13:** Climate Action

---

## 👥 Team Members & Roles
- **Reza Lotfi** (`lotfi@u.northwestern.edu`) — Team Coordinator | Task 2: Weather Data Lead & Modeling
- **Benameur Nehar** (`benameur.nehar@univ-tlemcen.dz`) — Task 3: EDA Plots, Modeling & Analysis Lead
- **Ruwaa Bahgat** (`ruwaabahgat@aun.edu.eg`) — Task 1: Generation Data Lead, Baseline Model & Presentation Lead

---

## 📊 Data Engineering & Features

### Core Data Sources
1. **ENTSO-E Transparency Platform:** Actual hourly solar electricity generation data for Greece.
2. **Open-Meteo Historical Weather API:** Hourly weather parameters extracted for 5 major Greek cities: **Athens, Thessaloniki, Patras, Heraklion, and Larissa**.

### Engineered Features
To capture temporal dynamics and weather variations, the following features are extracted and integrated:
- **Weather Input:** Shortwave radiation (solar irradiance), cloud cover, and ambient temperature.
- **Calendar Features:** Hour of day, day of year, day of week, and season.
- **Lag & Rolling Windows:** 24-hour target lag and rolling averages computed strictly using past values to eliminate data leakage.

---

## ⚙️ Model Pipeline

1. **Ingestion & Alignment:** Merging ENTSO-E and Open-Meteo datasets by standardizing all timestamps into a common **UTC** index.
2. **Data Cleaning:** Handling data gaps or missing values via targeted interpolation and forward-filling.
3. **Chronological Splitting:** Enforcing a strict time-based train/test split (e.g., historical 80% train / 20% test) to prevent chronological leakage.
4. **Baseline Benchmark:** Implementing a persistence baseline where tomorrow's hourly solar forecast equals today's exact hourly generation ($Y_{t+24} = Y_t$).
5. **ML Training:** Fitting supervised regressor algorithms (e.g., Random Forest, Gradient Boosting) using `scikit-learn`.

---

## 📈 Success Metrics
Models are thoroughly evaluated against the persistence baseline on the held-out test data using three primary metrics:
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **Coefficient of Determination ($R^2$)**

---

## 🚀 How to Run the Scripts

### Weather Data Collection
To extract the historical weather data for all 5 target Greek cities, run:
```bash
python greece_cities_weather_1yr_utc.csv
This query maps out an entire target year of data to output a structured file named greece_cities_weather_1yr_utc.csv.1
