import requests


class ApiURL(object):
    def __init__(self, url=None, **kwargs):
        self.url = url

    def request(self, data):
        pass


class Address(ApiURL):
    pass


HANDLERS = {
    'default': lambda self, name: super(DaDataClient, self).__getattribute__(name),
    'address': lambda self, name: Address(
        url = self.url + 'address'
    )
}


class DaDataClient(object):
    defaults = {
        'url': 'https://dadata.ru/api/v2/clean/',
    }

    def __init__(self, *args, **kwargs):
        for key, value in self.defaults.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattribute__(self, name):
        handler = HANDLERS.get(name, HANDLERS.get('default'))
        return handler(self, name)
