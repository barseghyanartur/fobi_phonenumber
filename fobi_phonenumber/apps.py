__title__ = 'fobi_phonenumber.apps'
__author__ = 'James Fenwick <jfenwick@tecaz.com'
__copyright__ = '2016-2017 Tecaz Ltd'
__license__ = 'GPL 2.0/LGPL 2.1'

try:
    from django.apps import AppConfig

    __all__ = ('Config',)

    class Config(AppConfig):
        name = 'fobi_phonenumber'
        label = 'fobi_phonenumber'

except ImportError:
    pass
