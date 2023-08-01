import os
from geopy.geocoders import Nominatim
import folium


class MapGenerator:
    def __init__(self, map_html_path):
        self.map_html_path = map_html_path

    def create_map_html(self):
        """
        This class is used to generate an HTML file that can display a map. 
        """
        if not os.path.exists(self.map_html_path):
            with open(self.map_html_path, 'w') as file:
                file.write("<html><body></body></html>")
        else:
            with open(self.map_html_path, 'r+') as file:
                file.truncate(0)
                file.write("<html><body></body></html>")


class MapCreator:
    def __init__(self, city):
        self.city = city
        self.geolocator = Nominatim(user_agent="myapp")
        self.latitude = None
        self.longitude = None
        self.map = None

    def get_coordinates(self):
        """
        This class is used to create a map using geographical coordinates for a given city.
        """
        location = self.geolocator.geocode(self.city)
        self.latitude = location.latitude
        self.longitude = location.longitude

    def create_map(self):
        self.map = folium.Map(
            location=[
                self.latitude,
                self.longitude],
            zoom_start=10)
        folium.Marker([self.latitude, self.longitude],
                      popup=self.city).add_to(self.map)

    def save_map(self, filename):
        self.map.save(filename)
