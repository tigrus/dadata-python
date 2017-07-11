# coding: utf-8
from .common import CommonTestCase


class SuggestionsTest(CommonTestCase):
    def test_suggestion_url(self):
        client = self.client
        # self.assertEqual(client.suggestions.address.url, "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address")
        self.assertEqual(client.suggestions.address.url, "https://dadata.ru/api/v2/suggest/address")

    def test_that_suggestion_url_is_not_private(self):
        self.assertEqual(self.client.suggestions.address.private, False)

    def test_that_assigned_data_is_query(self):
        self.client.suggest_address = "test"
        self.assertEqual(self.client.data, {'query' : 'test'})
