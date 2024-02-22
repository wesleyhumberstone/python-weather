from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Manchester"):

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?l&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(requests_url).json()

    # # City is not found by API
    # if not weather_data['cod'] == 200:
    #     return "city not found"

    return weather_data

if __name__ == "__main__":
    print('\n*** get current weather conditions***\n')

    city = input("\n please enter a city name: ")

    #check for empty str or str with only spaces
    if not bool(city.strip()):
        city = "London"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)