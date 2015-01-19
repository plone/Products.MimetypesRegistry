from Acquisition import aq_base
from ExtensionClass import Base
from Products.CMFCore.utils import getToolByName as _getToolByName
from zExceptions import BadRequest
from zope.interface import Attribute
from zope.interface import Interface
import logging
import os.path

# list and dict classes to use
from Persistence import PersistentMapping as DictClass
try:
    from ZODB.PersistentList import PersistentList as ListClass
except ImportError:
    from persistent.list import PersistentList as ListClass


# directory where template for the ZMI are located
_www = os.path.join(os.path.dirname(__file__), 'www')

FB_REGISTRY = None
_marker = []


logger = logging.getLogger('PortalTransforms')


def log(msg, severity=logging.INFO, id='PortalTransforms'):
    logger.log(severity, msg)


def implements(object, interface):
    return interface.providedBy(object)


def getToolByName(context, name, default=_marker):
    global FB_REGISTRY
    tool = _getToolByName(context, name, default)
    if name == 'mimetypes_registry' and tool is default:
        if FB_REGISTRY is None:
            from Products.MimetypesRegistry.MimeTypesRegistry \
                 import MimeTypesRegistry
            FB_REGISTRY = MimeTypesRegistry()
        tool = FB_REGISTRY
    return tool


__all__ = ('Base', 'log', 'DictClass', 'ListClass', 'getToolByName', 'aq_base',
           'Interface', 'Attribute', 'implements', '_www',
           'BadRequest', )
