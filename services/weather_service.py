import json
import urllib.parse
import urllib.request

def get_current_weather(city:str)->str:
    try:
        # -----------------------------
        # Geocoding API
        # -----------------------------
        geo_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
            f"?name={urllib.parse.quote(city)}&count=1"
        )
        with urllib.request.urlopen(geo_url) as response:
            geo_data= json.loads(response.read().decode())
        
        if "results" not in geo_data:
            return f"City not found: {city}"
        
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # -----------------------------
        # Weather API
        # -----------------------------
        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current=temperature_2m"
        )

        with urllib.request.urlopen(weather_url) as response:
            weather_data = json.loads(response.read().decode())

        temp = weather_data["current"]["temperature_2m"]

        return f"Weather in {city}: {temp}°C"

    except Exception as ex:
        return f"Error: {ex}"