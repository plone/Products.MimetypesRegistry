"""some common utilities
"""
from time import time
from types import UnicodeType, StringType

STRING_TYPES = (UnicodeType, StringType)

class TransformException(Exception):
    pass

class MimeTypeException(Exception):
    pass

try:
    import Zope
except ImportError:
    HAS_ZOPE = 0
else:
    HAS_ZOPE = 1

if HAS_ZOPE:
    from base_zope import *
else:
    from base_python import *

__all__ = ('Base', 'log', 'DictClass', 'ListClass', 'getToolByName',
           'Interface', 'Attribute', 'implements', 'skins_dir', 'aq_base',
           'HAS_ZOPE', 'time', 'Cache', 'TransformException', 
           'MimeTypeException', 'STRING_TYPES', )
