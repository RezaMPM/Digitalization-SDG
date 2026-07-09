import requests
import pandas as pd
import time

def fetch_weather_data(lat, lon, start_date, end_date):
    # Open-Meteo Historical API endpoint
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    # Define the payload based on project requirements
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "shortwave_radiation", "cloudcover"],
        "timezone": "UTC" 
    }
    
    # Fetch the data
    response = requests.get(url, params=params)
    response.raise_for_status() 
    data = response.json()
    
    # Extract the hourly data and convert to a pandas DataFrame
    hourly_data = data["hourly"]
    df = pd.DataFrame(hourly_data)
    
    # Convert the time column to datetime objects and set as index
    df['time'] = pd.to_datetime(df['time'], utc=True)
    df.set_index('time', inplace=True)
    
    return df

# Dictionary of major Greek cities and their coordinates
cities = {
    "Athens": (37.9838, 23.7278),
    "Thessaloniki": (40.6403, 22.9356),
    "Patras": (38.2500, 21.7333),
    "Heraklion": (35.3403, 25.1344),
    "Larissa": (39.6417, 22.4167)
}

# Set the timeframe for the baseline year
year_start = "2023-01-01" 
year_end = "2023-12-31"

all_weather_data = []

# Loop through each city and fetch the data
for city, (lat, lon) in cities.items():
    print(f"Fetching data for {city}...")
    city_df = fetch_weather_data(lat, lon, year_start, year_end)
    
    # Add a column to identify the city in the merged dataset
    city_df['city'] = city
    all_weather_data.append(city_df)
    
    # A brief pause to respect the API's rate limits
    time.sleep(1)

# Combine all cities into a single DataFrame
final_weather_df = pd.concat(all_weather_data)

# Preview the combined data
print(final_weather_df.head())
print("\nData points per city:")
print(final_weather_df['city'].value_counts())

# Save to CSV for the Week 7 deliverable 
final_weather_df.to_csv("greece_cities_weather_1yr_utc.csv")
print("\nData successfully saved to greece_cities_weather_1yr_utc.csv")