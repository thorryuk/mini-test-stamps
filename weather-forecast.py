import requests
from datetime import datetime

API_KEY = "2e4b04b2c26ddc8d557d5fd8906e1341"
CITY = "Jakarta"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    
    forecasts = data["list"]
    daily_temps = {}

    for forecast in forecasts:
        dt = forecast["dt"]
        temp = forecast["main"]["temp"]
        date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
        time = datetime.utcfromtimestamp(dt).strftime('%H:%M:%S')
        if date not in daily_temps and time == "12:00:00":
            daily_temps[date] = temp

    print("Weather Forecast:")
    for date, temp in daily_temps.items():
        day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%a, %d %b %Y')
        print(f"{day_name}: {temp:.2f}°C")
else:
    print(f"Failed to fetch weather data. HTTP Status Code: {response.status_code}")
