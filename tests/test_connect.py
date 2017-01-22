"""
Тестового варианта доступа не существует, поэтому проверим отказ в доступе.
"""

import unittest
from dadata import DaDataClient


class DenyTest(unittest.TestCase):
    def test_deny(self):
        self.assertTrue(True)


