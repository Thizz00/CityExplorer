import requests
import json
from dotenv import load_dotenv
import os


class CityDataFetcher:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_city_data(self, city_name):
        """
        This provided function, get_city_data, is used to retrieve city data from an external API.
        It utilizes a RESTful API architecture.
        """
        load_dotenv()
        api_secret = os.getenv('API_SECRET')
        api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(
            city_name)
        response = requests.get(api_url, headers={'X-Api-Key': api_secret})

        if response.status_code == requests.codes.ok:
            data = response.text
            parsed_data = json.loads(data)
            return parsed_data[0]
        else:
            return ("Error: API request failed.")
