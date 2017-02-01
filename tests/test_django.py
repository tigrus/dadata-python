# coding: utf-8
from .common import CommonTestCase
from mock import patch, MagicMock
import dadata.plugins.django

"""
Monkey Patching.
"""
def get_settings():
    class Settings(object):
        pass
    s = Settings()
    s.DADATA_KEY = "key"
    s.DADATA_SECRET = "secret"
    return s

dadata.plugins.django.get_settings = get_settings

class DjangoTest(CommonTestCase):
    """
    Проверяем, что создан клиент с настройками от django
    """
    @patch('dadata.plugins.django.get_settings', get_settings)
    def test_django_init(self):
        client = dadata.plugins.django.DjangoDaDataClient()
        self.assertEqual(client.key, "key")
        pass
