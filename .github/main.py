import requests

def get_weather(city_name):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
