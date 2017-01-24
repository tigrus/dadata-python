# coding: utf-8
import unittest
import random
from dadata import DaDataClient
from dadata import LimitExceed, Errors


class UrlBuildTest(unittest.TestCase):
    """
    Проверяем создание урла для запроса
    """
    def setUp(self):
        self.client = DaDataClient()

    def test_address_url(self):
        url = self.client.address.url
        correct_url = self.client.url + '/clean/address'
        self.assertEqual(url, correct_url)

    def test_request_no_key(self):
        result = self.client.address.request()
        self.assertEqual(result, Errors.CLIENT_NO_KEY)

    def test_request_no_secret(self):
        client = DaDataClient(key="anykey")
        result = client.address.request()
        self.assertEqual(result, Errors.CLIENT_NO_SECRET)

    def test_request_no_data(self):
        client = DaDataClient(key="anykey", secret="anysec")
        result = client.address.request()
        self.assertEqual(result, Errors.CLIENT_NO_DATA)



class DataSetTest(unittest.TestCase):
    """
    Проверяем параметры и их лимиты
    """
    def setUp(self):
        self.client = DaDataClient()

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

    def test_address_many_set_over_limit(self):
        try:
            self.client.address.many = ["Berkley Street 10", "Another Nice Street", "10", "20"]
        except LimitExceed as e:
            self.assertTrue(e)
        self.assertFalse(self.client.address.many)
