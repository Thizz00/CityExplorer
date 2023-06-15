import unittest
from unittest.mock import MagicMock
from Api.city_data_fetcher import CityDataFetcher
from Api.city_info import CityName

class CityNameTest(unittest.TestCase):
    def setUp(self):
        self.city_name = CityName()

    def test_get_city_name(self):
        city_data_fetcher_mock = MagicMock()
        city_data_fetcher_mock.get_city_data.return_value = {'name': 'New York'}
        CityDataFetcher.__new__ = MagicMock(return_value=city_data_fetcher_mock)

        city_name = self.city_name.get_city_name('New York')

        self.assertEqual(city_name, 'New York')
        city_data_fetcher_mock.get_city_data.assert_called_once_with('New York')

    def test_get_city_name_invalid_data(self):
        city_data_fetcher_mock = MagicMock()
        city_data_fetcher_mock.get_city_data.return_value = None
        CityDataFetcher.__new__ = MagicMock(return_value=city_data_fetcher_mock)

        city_name = self.city_name.get_city_name('Invalid City')

        self.assertIsNone(city_name)
        city_data_fetcher_mock.get_city_data.assert_called_once_with('Invalid City')

if __name__ == '__main__':
    unittest.main()
