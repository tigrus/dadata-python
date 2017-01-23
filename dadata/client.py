import requests
from copy import deepcopy

"""
Ограничения:
    не более 1 ФИО,
    3 адресов,
    3 телефонов,
    3 email
"""
EMAIL_LIMIT = 3
PHONE_LIMIT = 3
ADDRESS_LIMIT = 3
FIO_LIMIT = 1

"""
Helper Mixins
"""
class ManyOneMixin(object):
    def _get_one(self):
        return self.data[0] if self.data else None

    def _set_one(self, value):
        self.data.append(value)

    one = property(_get_one, _set_one)

    def _get_many(self):
        return self.data

    def _set_many(self, value):
        self.data.extend(value)

    many = property(_get_many, _set_many)


"""
Обертка над Dadata API
"""
class ApiURL(ManyOneMixin):
    limit = 1

    def __init__(self, url=None, **kwargs):
        self.url = url
        self.data = []



class Address(ApiURL):
    pass


class DaDataClient(object):
    defaults = {
        'url': 'https://dadata.ru/api/v2/clean/',
    }

    def __init__(self, *args, **kwargs):
        for key, value in self.defaults.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.address = Address(
            url = self.url + 'address'
        )
