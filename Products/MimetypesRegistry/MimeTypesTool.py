"""this file act as a redirector to provide the correct class if we are running
zope or not
"""
__revision__ = '$Id: MimeTypesTool.py,v 1.1 2004/05/22 16:30:27 tiran Exp $'

from common import HAS_ZOPE

if HAS_ZOPE:
    from Products.MimetypesRegistry.zope.MimeTypesTool import MimeTypesTool
else:
    from MimeTypesRegistry import MimeTypesRegistry as MimeTypesTool
