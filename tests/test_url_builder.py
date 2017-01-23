# coding: utf-8
"""
Проверяем создание урла для запроса
"""
import unittest
from dadata import DaDataClient


class UrlBuildTest(unittest.TestCase):
    def setUp(self):
        self.client = DaDataClient()

    def test_address_url(self):
        url = self.client.address.url
        correct_url = self.client.defaults.get('url') + 'address'
        self.assertEqual(url, correct_url)
