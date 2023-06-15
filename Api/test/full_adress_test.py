import unittest
from Api.full_adress import AdressName

class AddressNameTestCase(unittest.TestCase):
    def setUp(self):
        self.name = "Melbourne"
        self.address = "Melbourne, City of Melbourne, Victoria, Australia"
        self.address_name = AdressName(self.name)

    def test_get_address(self):
        self.assertEqual(self.address_name.get_address(), self.address)

if __name__ == '__main__':
    unittest.main()
