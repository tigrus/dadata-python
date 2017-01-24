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
Errors
"""
class Errors:
    CLIENT_NO_KEY = 600
    CLIENT_NO_SECRET = 601
    CLIENT_NO_DATA = 602

"""
Exceptions
"""
class LimitExceed(Exception):
    pass


"""
Helper Mixins
"""
class ManyOneMixin(object):
    def _get_one(self):
        return self.data[0] if self.data else None

    def _set_one(self, value):
        self.data = []
        self.data.append(value)

    one = property(_get_one, _set_one)

    def _get_many(self):
        return self.data

    def _set_many(self, value):
        self.data = []
        if len(value) > self.limit:
            raise LimitExceed('Ограничение превышено. Введено %s значений из %s' % (len(value), self.limit))
        self.data.extend(value)

    many = property(_get_many, _set_many)


"""
Обертка над Dadata API
"""
class ApiURL(ManyOneMixin):
    limit = 1
    url = ''
    data = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def request(self):
        if not self.key:
            return Errors.CLIENT_NO_KEY
        if not self.secret:
            return Errors.CLIENT_NO_SECRET
        if not self.data:
            return Errors.CLIENT_NO_DATA


class Clean(ApiURL):
    def __init__(self, *args, **kwargs):
        super(Clean, self).__init__(*args, **kwargs)
        kwargs['url'] = kwargs['url'] + '/address'
        self.address = Address(**kwargs)


class Address(ApiURL):
    limit = ADDRESS_LIMIT


class DaDataClient(object):
    url = 'https://dadata.ru/api/v2'
    key = ''
    secret = ''

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.clean = Clean(
            url = self.url + '/clean',
            key = self.key,
            secret = self.secret,
        )

    @property
    def address(self):
        return self.clean.address

