# -------------------------------------------------
# Exercise 4: Weather Data Fetcher & Analyzer
# -------------------------------------------------
# This program:
# 1. Fetches weather data using OpenWeatherMap API
# 2. Analyzes temperature conditions
# 3. Adds alerts for wind speed and humidity
# 4. Logs weather information into a CSV file
# 5. Uses environment variables for API security
# -------------------------------------------------

import requests
import os


def fetch_weather(city):
    """
    Fetch weather data for a given city using OpenWeatherMap API
    """
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
            raise ValueError("API key not found in environment variables.")

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric"
        )

        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError:
        print("Error: Invalid city name or API request.")
    except requests.exceptions.RequestException:
        print("Error: Network issue occurred.")
    except Exception as e:
        print("Error:", e)

    return None


def analyze_weather(weather_data):
    """
    Analyze weather conditions based on temperature,
    wind speed, and humidity
    """
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    if temp <= 10:
        summary = "Cold (≤10°C)"
    elif 11 <= temp <= 24:
        summary = "Mild (11–24°C)"
    else:
        summary = "Hot (≥25°C)"

    if wind_speed > 10:
        summary += " | High wind alert!"
    if humidity > 80:
        summary += " | Humid conditions!"

    return summary


def log_weather(city, filename):
    """
    Fetches weather data, analyzes it,
    and appends results to a CSV file
    """
    data = fetch_weather(city)

    if data:
        temperature = data["main"]["temp"]
        summary = analyze_weather(data)

        with open(filename, "a") as file:
            file.write(f"{city},{temperature},{summary}\n")

        print("\nWeather Data Logged Successfully")
        print(f"City: {city}")
        print(f"Temperature: {temperature} °C")
        print(f"Condition: {summary}")


# -------------------------------
# Program Execution
# -------------------------------

city_name = input("Enter city name: ")
log_weather(city_name, "weather_log.csv")
