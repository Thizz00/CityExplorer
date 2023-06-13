import requests
import json
from dotenv import load_dotenv
import os

class WeatherInfo:
    def __init__(self, city_name):
        self.city_name = city_name

    def get_weather(self):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={api_key}'
        response = requests.get(api_url)
        response_json = response.json()
        
        if response.status_code == requests.codes.ok:
            try:
                weather_main = response_json['weather'][0]['main']
                return weather_main
            except KeyError:
                 return("Error: Unable to retrieve weather information.")
        else:
            return("Error: API request failed.")
