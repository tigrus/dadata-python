# coding: utf-8
"""
Проверяем создание урла для запроса
"""
import unittest
import random
from dadata import DaDataClient


class UrlBuildTest(unittest.TestCase):
    def setUp(self):
        self.client = DaDataClient()

    def test_address_url(self):
        url = self.client.address.url
        correct_url = self.client.defaults.get('url') + 'address'
        self.assertEqual(url, correct_url)

    def test_address_one_empty(self):
        self.assertEqual(self.client.address.one, None)

    def test_address_one_set(self):
        self.client.address.one = "Berkley Street 10"
        self.assertEqual(self.client.address.one, "Berkley Street 10")

    def test_address_many_set(self):
        self.client.address.many = ["Berkley Street 10", "Another Nice Street"]
        self.assertEqual(self.client.address.many, self.client.address.data)
        self.assertEqual(self.client.address.many, ["Berkley Street 10", "Another Nice Street"])
        self.assertEqual(self.client.address.one, "Berkley Street 10")
