import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the name of the city:\n")

url = f"http://api.weatherapi.com/v1/current.json?key=92181aba61044f0397863025251106&q={city}"

r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:    
    wdic = json.loads(r.text)
    
    location = wdic["location"]
    current = wdic["current"]
    
    weather_info = f"""
    Weather details for {location['name']}, {location['region']}, {location['country']}:
    - Temperature: {current['temp_c']}°C ({current['temp_f']}°F)
    - Condition: {current['condition']['text']}
    - Wind: {current['wind_kph']} km/h ({current['wind_mph']} mph) from {current['wind_dir']}
    - Humidity: {current['humidity']}%
    - Pressure: {current['pressure_mb']} mb ({current['pressure_in']} in)
    - Visibility: {current['vis_km']} km ({current['vis_miles']} miles)
    - Feels like: {current['feelslike_c']}°C ({current['feelslike_f']}°F)
    - UV Index: {current['uv']}
    """


    print(weather_info)

    engine.say(weather_info)
    engine.runAndWait()

else:
    error_message = "Error: Unable to retrieve weather data. Please check the city name or try again later."
    print(error_message)
    engine.say(error_message)
    engine.runAndWait()
