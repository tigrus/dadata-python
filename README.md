Unofficial Python dadata.ru Client [![Build Status](https://travis-ci.org/tigrus/dadata-python.svg?branch=master)](https://travis-ci.org/tigrus/dadata-python)
===============================================

## Install

```
$ pip install -e git+https://github.com/tigrus/dadata-python#egg=dadata
```

## Usage

```
>>> from dadata import DaDataClient
>>> client = DaDataClient(
    key = '',
    secret = '',
)

>>> # You can assign one address
>>> client.address = "мск сухонска 11/-89"

>>> # You can assign multiple addresses
>>> client.address = ["мск сухонска 11/-89", "спб невский 18"]

>>> #Now let's perform request..
>>> client.address.request()

>>> #Now we will have first result in `client.result`
>>> client.result.region_kladr_id
'7700000000000'

>>> #However we can reprocess data by our own desire - result from API saved in 
>>> client.response.content
```

## Usage With Django

In `settings.py`:
```
DADATA_KEY = ""
DADATA_SECRET = ""
```

In project:
```
>>> from dadata.plugins.django import DjangoDaDataClient
>>> client = DjangoDaDataClient()

>>> # Now using as regular client..
>>> client.address = "мск сухонска 11/-89"
...
```

## Suggestions Usage


```
>>> client.suggest_address = "194292, Санкт-Петербург г, 1-й Верхний пер, дом № 12, литера Б"
>>> client.suggestions.address.request()
>>> # Now we have list of suggestions in client.result
>>> client.result.suggestions[0].get('data').get('kladr_id')
'7800000000015870028'
```
