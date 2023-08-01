from Api.city_data_fetcher import CityDataFetcher


class PopulationInfo:
    def get_population(self, city_name):
        city_data = CityDataFetcher().get_city_data(city_name)
        if city_data is not None:
            return (city_data['population'])
