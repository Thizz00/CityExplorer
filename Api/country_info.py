from geopy.geocoders import Nominatim

class AdressName:
    def __init__(self, name):
        self.name = name
        self.geolocator = Nominatim(user_agent="geoapiExercises")
        self.location = None

    def get_address(self):
        self.location = self.geolocator.geocode(self.name)
        if self.location is not None:
            return(self.location.address)
        else:
            return(None)


