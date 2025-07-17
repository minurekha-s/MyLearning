# Weather App Project
# This script displays the current weather for a given city using the OpenWeatherMap API.
# Demonstrates user input, HTTP requests, JSON parsing, and error handling.

import requests

API_KEY = "f0565cfcabad812ca0cb7f4a2fa27328"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            print(f"Current weather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Description: {desc}")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather.')}")
    except Exception as e:
        print(f"Error: {e}")

def weather_app():
    print("=== Weather App ===")
    city = input("Enter city name: ").strip()
    get_weather(city)

if __name__ == "__main__":
    weather_app()
