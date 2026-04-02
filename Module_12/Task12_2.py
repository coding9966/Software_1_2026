import requests

API_KEY = "ad00b519568ca28e60f6e83086af930f"

city = input("Enter municipality name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)
print("Full response:", response.text)

if response.status_code == 200:
    data = response.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather: {description}")
    print(f"Temperature: {temperature} °C")