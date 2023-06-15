import unittest
from unittest.mock import MagicMock
from Api.city_data_fetcher import CityDataFetcher
from Api.capital_info import CapitalInfo

class TestCapitalInfo(unittest.TestCase):
    def setUp(self):
        self.city_data_fetcher = CityDataFetcher()
        self.capital_info = CapitalInfo()

    def test_is_capital(self):
        city_name = "Warsaw"
        city_data = {'is_capital': True}
        self.city_data_fetcher.get_city_data = MagicMock(return_value=city_data)

        result = self.capital_info.is_capital(city_name)

        self.assertEqual(result, 'Yes')
        self.city_data_fetcher.get_city_data.assert_called_once_with(city_name)

    def test_is_not_capital(self):
        city_name = "Kraków"
        city_data = {'is_capital': False}
        self.city_data_fetcher.get_city_data = MagicMock(return_value=city_data)

        result = self.capital_info.is_capital(city_name)

        self.assertEqual(result, 'No')
        self.city_data_fetcher.get_city_data.assert_called_once_with(city_name)

    def test_city_data_not_found(self):
        city_name = "fasfasf"
        self.city_data_fetcher.get_city_data = MagicMock(return_value=None)

        result = self.capital_info.is_capital(city_name)

        self.assertIsNone(result)
        self.city_data_fetcher.get_city_data.assert_called_once_with(city_name)

if __name__ == '__main__':
    unittest.main()
