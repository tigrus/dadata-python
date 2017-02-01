# coding: utf-8
from .common import CommonTestCase
from dadata import LimitExceed, Errors


class UrlBuildTest(CommonTestCase):
    """
    Проверяем создание урла для запроса
    """
    def test_address_url(self):
        url = self.client.address.url
        correct_url = self.client.url + '/clean/address'
        self.assertEqual(url, correct_url)

    def test_request_no_key(self):
        result = self.client.address.request()
        self.assertEqual(result, Errors.CLIENT_NO_KEY)

    def test_request_no_secret(self):
        result = self.client_with_key.address.request()
        self.assertEqual(result, Errors.CLIENT_NO_SECRET)

    def test_request_no_data(self):
        result = self.client_with_key_secret.address.request()
        self.assertEqual(result, Errors.CLIENT_NO_DATA)


class DataSetTest(CommonTestCase):
    """
    Проверяем параметры и их лимиты
    """
    def test_address_one_empty(self):
        self.assertEqual(self.client.address.one, None)

    def test_address_one_set(self):
        self.client.address = "Berkley Street 10"
        self.assertEqual(self.client.address.one, "Berkley Street 10")

    def test_address_many_set(self):
        self.client.address = ["Berkley Street 10", "Another Nice Street"]
        self.assertEqual(self.client.address.many, self.client.data)
        self.assertEqual(self.client.address.many, ["Berkley Street 10", "Another Nice Street"])
        self.assertEqual(self.client.address.one, "Berkley Street 10")

    def test_address_many_set_over_limit(self):
        try:
            self.client.address.many = ["Berkley Street 10", "Another Nice Street", "10", "20"]
        except LimitExceed as e:
            self.assertTrue(e)
        self.assertFalse(self.client.address.many)
