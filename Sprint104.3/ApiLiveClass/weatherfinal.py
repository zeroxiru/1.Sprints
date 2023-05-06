
import requests

url = "https://api.openweathermap.org/data/2.5/weather"

query_params = {
    "q": "New York,US",
    "appid": "your_api_key",
    "units": "metric"
}

# List of ten cities to get weather data for
cities = ["london,Uk", "Los Angeles,US", "Chicago,US", "Houston,US", "Phoenix,US", "Philadelphia,US", "San Antonio,US", "San Diego,US", "Dallas,US", "San Jose,US"]

# Dictionary to store temperature data for each city
temperatures = {}

# Loop through each city and get the current temperature
for city in cities:
    query_params["q"] = city
    response = requests.get(url, params=query_params)
    data = response.json()
    if "main" in data:
        temperatures[city] = data["main"]["temp"]
    else:
        print(f"No weather data available for {city}.")

# Find the city with the highest temperature
if len(temperatures) > 0:
    hottest_city = max(temperatures, key=temperatures.get)
    print(f"The hottest city is {hottest_city} with a temperature of {temperatures[hottest_city]} degrees Celsius.")
else:
    print("No temperature data available for any city.")