__title__ = 'fobi_phonenumber.fobi_form_elements'
__author__ = 'James Fenwick <jfenwick@tecaz.com'
__copyright__ = '2016-2017 Tecaz Ltd'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'PhoneNumberPlugin',
)

from fobi.base import form_element_plugin_registry

from .base import PhoneNumberPlugin


form_element_plugin_registry.register(PhoneNumberPlugin)
