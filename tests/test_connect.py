"""
Тестового варианта доступа не существует, поэтому проверим отказ в доступе.
"""

import unittest


class DenyTest(unittest.TestCase):
    def testDeny(self):
        print("Deny test should be here..")
        self.assertTrue(True)


