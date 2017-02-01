Unofficial Python dadata.ru Client [![Build Status](https://travis-ci.org/tigrus/dadata-python.svg?branch=master)](https://travis-ci.org/tigrus/dadata-python)
===============================================

## Usage

```
>>> from dadata import DaDataClient
>>> client = DaDataClient(
    key = '',
    secret = '',
)

>>> # You can assign one address
>>> client.address.one = "мск сухонска 11/-89"

>>> #You can assign multiple addresses
>>> client.address.many = ["мск сухонска 11/-89", "спб невский 18"]

>>> #Now let's perform request..
>>> client.address.request()

>>> #Now we will have first result in `client.result`
>>> client.result.region_kladr_id
'7700000000000'

>>> #However we can reprocess data by our own desire - result from API saved in 
>>> client.response.content
```

