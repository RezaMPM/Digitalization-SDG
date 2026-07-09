
import requests
import pandas as pd

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

# Set parameters for Athens and your target year
athens_lat = 37.9838
athens_lon = 23.7278
year_start = "2023-01-01" # Ensure this matches Ruwaa's generation data year
year_end = "2023-12-31"

# Execute function
athens_weather_df = fetch_weather_data(athens_lat, athens_lon, year_start, year_end)

# Preview the data
print(athens_weather_df.head())

# Save to CSV for the Week 7 deliverable 
athens_weather_df.to_csv("athens_weather_1yr_utc.csv")