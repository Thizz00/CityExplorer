from Api.city_data_fetcher import CityDataFetcher
class CapitalInfo:
    def is_capital(self, city_name):
        city_data = CityDataFetcher().get_city_data(city_name)
        if city_data is not None:
            is_capital = 'Yes' if city_data['is_capital'] == True else 'No'
            return(is_capital)
        else:
            return(None)
