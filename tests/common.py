import unittest
from dadata import DaDataClient


class CommonTestCase(unittest.TestCase):
    def setUp(self):
        self.client = DaDataClient()
        self.client_with_key = DaDataClient(key="anykey")
        self.client_with_key_secret = DaDataClient(key="anykey", secret="anysec")
