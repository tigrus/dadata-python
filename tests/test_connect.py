# coding: utf-8
"""
Тестового варианта доступа не существует, поэтому проверим отказ в доступе.
"""
from .common import CommonTestCase


class DenyTest(CommonTestCase):
    def test_that_client_has_session(self):
        self.assertTrue(self.client.session)
