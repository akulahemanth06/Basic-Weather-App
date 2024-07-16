import requests

def get_weather(city):
    api_key = "e8bc5f8e4f513f628d3111bcc89be552"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") != "404":
        if "main" in data:
            main = data["main"]
            weather = data["weather"][0]

            # Manually convert temperature from Kelvin to Celsius
            temperature = main["temp"] - 273.15
            pressure = main["pressure"]
            humidity = main["humidity"]
            description = weather["description"]

            print(f"City: {city}")
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description.capitalize()}")
        else:
            print("Unexpected response format:", data)
    else:
        print("City Not Found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
