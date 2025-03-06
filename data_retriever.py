import requests
import json 

# Define the API endpoint and parameters
url = "https://archive-api.open-meteo.com/v1/archive?latitude=22.2783&longitude=114.1747&start_date=2020-01-01&end_date=2025-03-01&hourly=relative_humidity_2m&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&timezone=Asia%2FSingapore"
params = {
    "latitude": 22.2783,  # Latitude for Hong Kong
    "longitude": 114.1747,  # Longitude for Hong Kong
    "daily": ["temperature_2m_mean," "precipitation_sum", "wind_speed_10m_max"],  # Request daily data
    "hourly": ["relative_humidity_2m"],  # Request hourly data
    "start_date": "2020-01-01",  # Start date
    "end_date": "2025-03-01",  # End date
    "timezone": "auto"  # Automatically detect the timezone
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    with open("weather.json", "w") as file:
        json.dump(data,file,indent=4)
else:
    print(f"Failed to retrieve data: {response.status_code}")