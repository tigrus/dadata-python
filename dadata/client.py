import requests


class DaDataClient(object):
    defaults = {
        'url': 'https://dadata.ru/api/v2/clean/',
    }

    def __init__(self, *args, **kwargs):
        for key, value in self.defaults.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            setattr(self, key, value)
