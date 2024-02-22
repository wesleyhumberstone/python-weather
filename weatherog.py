import os
import requests
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

def get_current_weather():
    print('\n*** get current weather conditions ***\n')

    city = input('\n please enter a city name:\n')

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?l&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #print(requests_url)

    weather_data = requests.get(requests_url).json()

    #pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')

if __name__ == "__main__":
    get_current_weather()