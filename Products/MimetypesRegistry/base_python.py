"""some common utilities
"""

# base class
class Base : pass

# logging function
from sys import stderr
def log(msg, severity=None, id=None):
    print >>stderr, msg

# list and dict classes to use
from UserDict import UserDict as DictClass
from UserList import UserList as ListClass

skins_dir = None # XXX
_www = None

def aq_base(obj):
    return obj

# getToolByName should only have to return the mime types registry in this
# mode
_MTR = None
def getToolByName(self, name):
    assert name == 'mimetypes_registry'
    global _MTR
    if _MTR is None:
        from Products.MimetypesRegistry.MimeTypesTool import MimeTypesTool
        _MTR = MimeTypesTool(fill=1)
    return _MTR

class Interface:
    """dummy interface class
    """
    pass

class Attribute:
    """dummy attribute class
    """
    def __init__(self, doc):
        self.doc = doc
        
    def __repr__(self):
        return self.doc

from types import ListType, TupleType
def implements(object, interface):
    if hasattr(object, "__implements__") and \
           (interface == object.__implements__ or \
            (type(object.__implements__) in (ListType, TupleType) and \
             interface in object.__implements__)):
        return 1
    return 0

__all__ = ('Base', 'log', 'DictClass', 'ListClass', 'getToolByName', 'aq_base',
           'Interface', 'Attribute', 'implements', 'skins_dir', '_www', )
