# ============================================
# Week 11 Lab: EU Capitals Weather Data Collector
# Beginner-friendly version
# ============================================

import requests   # Used to call the weather API
import json       # Used to save data in JSON format
import time       # Used to add delay between API calls

# --------------------------------------------
# Weather code to readable text mapping
# --------------------------------------------
weather_code_meaning = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    95: "Thunderstorm"
}

# --------------------------------------------
# EU Capitals list (DO NOT CHANGE)
# --------------------------------------------
eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czech Republic", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1699, "lon": 24.9384},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8997, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]


# --------------------------------------------
# Dictionary to store all collected data
# --------------------------------------------
all_weather_data = {}

print("Starting EU Capitals Weather Collection...\n")

# --------------------------------------------
# Loop through each capital city
# --------------------------------------------
for capital in eu_capitals:
    city = capital["city"]
    country = capital["country"]
    latitude = capital["lat"]
    longitude = capital["lon"]

    print(f"Fetching weather data for {city}, {country}...")

    # Open-Meteo API URL
    api_url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true"
        "&hourly=temperature_2m,precipitation_probability,weathercode"
        "&forecast_days=1"
        "&timezone=auto"
    )

    try:
        # Send request to the API
        response = requests.get(api_url, timeout=10)

        # Convert response to JSON
        data = response.json()

        # -------------------------
        # Extract current weather
        # -------------------------
        current = data["current_weather"]
        weather_code = current["weathercode"]

        current_weather = {
            "temperature": current["temperature"],
            "windspeed": current["windspeed"],
            "weathercode": weather_code,
            "condition": weather_code_meaning.get(weather_code, "Unknown"),
            "time": current["time"]
        }

        # -------------------------
        # Extract hourly forecast
        # -------------------------
        hourly_forecast = []

        times = data["hourly"]["time"]
        temperatures = data["hourly"]["temperature_2m"]
        rain_probs = data["hourly"]["precipitation_probability"]
        codes = data["hourly"]["weathercode"]

        for i in range(len(times)):
            hourly_forecast.append({
                "time": times[i],
                "temperature": temperatures[i],
                "precipitation_probability": rain_probs[i],
                "weathercode": codes[i]
            })

        # -------------------------
        # Store city data
        # -------------------------
        all_weather_data[city] = {
            "country": country,
            "coordinates": {
                "latitude": latitude,
                "longitude": longitude
            },
            "current_weather": current_weather,
            "hourly_forecast": hourly_forecast
        }

        print(f"Data collected for {city}\n")

    except Exception as error:
        # Handle any error safely
        print(f"Failed to fetch data for {city}: {error}\n")


    # Respect API rate limits
    time.sleep(1)

# --------------------------------------------
# Save all data to JSON file
# --------------------------------------------
with open("eu_weather_data.json", "w", encoding="utf-8") as file:
    json.dump(all_weather_data, file, indent=4)

print("Weather data collection completed!")
print("Data saved to 'eu_weather_data.json'")
