import requests
import datetime
import json

# Coordinates for cities (Open-Meteo requires lat/lon)
cities = {
    "Kathmandu": (27.7172, 85.3240),
    "Pokhara": (28.2096, 83.9856),
    "Butwal": (27.7006, 83.4500),
    "Biratnagar": (26.4525, 87.2718),
}

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(city, lat, lon):
    # Today and yesterday dates
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,windspeed_10m,weathercode",
        "timezone": "auto",
        "start_date": yesterday.isoformat(),
        "end_date": today.isoformat()
    }

    res = requests.get(BASE_URL, params=params)
    data = res.json()

    # Current weather
    current = data["current_weather"]
    temp = current["temperature"]
    wind = current["windspeed"]
    code = current["weathercode"]

    # Hourly forecast (next 6 hours)
    hourly = data["hourly"]
    times = hourly["time"][:6]
    temps = hourly["temperature_2m"][:6]
    winds = hourly["windspeed_10m"][:6]
    codes = hourly["weathercode"][:6]

    forecast = [
        {"time": t, "temp": temp, "wind": w, "code": c}
        for t, temp, w, c in zip(times, temps, winds, codes)
    ]

    # Compare today vs yesterday (avg temp)
    today_temps = hourly["temperature_2m"][-24:]  # last 24 hours
    yesterday_temps = hourly["temperature_2m"][:-24]

    today_avg = sum(today_temps)/len(today_temps)
    yest_avg = sum(yesterday_temps)/len(yesterday_temps)

    return {
        "city": city,
        "temperature": temp,
        "wind": wind,
        "weathercode": code,
        "forecast": forecast,
        "today_avg_temp": today_avg,
        "yesterday_avg_temp": yest_avg
    }

# Collect data for all cities
reports = []
for city, (lat, lon) in cities.items():
    reports.append(get_weather(city, lat, lon))

# Find hottest, coldest, windiest
hottest = max(reports, key=lambda x: x["temperature"])
coldest = min(reports, key=lambda x: x["temperature"])
windiest = max(reports, key=lambda x: x["wind"])

summary = {
    "timestamp": datetime.datetime.now().isoformat(),
    "reports": reports,
    "hottest_city": hottest["city"],
    "coldest_city": coldest["city"],
    "windiest_city": windiest["city"]
}

# Save to JSON
with open("weather_report.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Weather report saved to weather_report.json")
