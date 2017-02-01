# coding : utf-8
import sys
from dadata import DaDataClient

def get_settings():
    from django.conf import settings
    return settings


class DjangoDaDataClient(DaDataClient):
    def __init__(self, *args, **kwargs):
        settings = get_settings()
        super(DjangoDaDataClient, self).__init__(
            key=settings.DADATA_KEY,
            secret=settings.DADATA_SECRET,
        )

