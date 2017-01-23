# coding: utf-8
"""
Проверяем конфигурируемость клиента
"""
import unittest
from dadata import DaDataClient


class DefaultsTest(unittest.TestCase):
    def setUp(self):
        self.client = DaDataClient()

    def test_url(self):
        self.assertEqual(self.client.url, self.client.url)

    def test_url_override(self):
        client = DaDataClient(url='http://myurl')
        self.assertEqual(client.url, 'http://myurl')
