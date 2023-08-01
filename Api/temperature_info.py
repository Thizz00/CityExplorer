import requests
import json
from dotenv import load_dotenv
import os


class TemperatureInfo:
    def __init__(self, city_name):
        self.city_name = city_name

    def get_temperature(self):
        """
        The given function get_temperature(self) is a method defined within a class.
        It retrieves the current temperature in Celsius for a specified city using the OpenWeatherMap API.
        The architecture used here is RESTful API architecture.
        """
        load_dotenv()
        api_key = os.getenv('API_KEY')
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={api_key}'
        response = requests.get(api_url)
        response_json = response.json()

        if response.status_code == requests.codes.ok:
            try:
                temperature_in_kelvin = response_json['main']['temp']
                temperature_in_celsius = temperature_in_kelvin - 272.15
                return str(round(temperature_in_celsius)) + '°C'
            except KeyError:
                return ("Error: Unable to retrieve temperature information.")
        else:
            return ("Error: API request failed.")
