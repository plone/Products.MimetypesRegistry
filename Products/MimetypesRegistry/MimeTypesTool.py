"""this file act as a redirector to provide the correct class if we are running
zope or not
"""
from common import HAS_ZOPE

if HAS_ZOPE:
    from Products.MimetypesRegistry.zope.MimeTypesTool import MimeTypesTool
else:
    from MimeTypesRegistry import MimeTypesRegistry as MimeTypesTool
