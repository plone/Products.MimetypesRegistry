__version__ = (1, 3, 2, 4)

from Products.MimetypesRegistry import MimeTypesRegistry
from Products.MimetypesRegistry.common import skins_dir

GLOBALS = globals()
PKG_NAME = 'MimetypesRegistry'

tools = (
    MimeTypesRegistry.MimeTypesRegistry,
    )

# XXX backward compatibility tricks to make old PortalTransform based Mimetypes
# running (required)
import sys
from Products.MimetypesRegistry import mime_types
sys.modules['Products.PortalTransforms.mime_types'] = mime_types

from Products.MimetypesRegistry import MimeTypeItem
sys.modules['Products.PortalTransforms.MimeTypeItem'] = MimeTypeItem

from Products.MimetypesRegistry import MimeTypeItem
sys.modules['Products.PortalTransforms.zope.MimeTypeItem'] = MimeTypeItem
sys.modules['Products.MimetypesRegistry.zope.MimeTypeItem'] = MimeTypeItem

def initialize(context):
    from Products.CMFCore.DirectoryView import registerDirectory
    registerDirectory(skins_dir, GLOBALS)
    
    from Products.CMFCore import utils
    utils.ToolInit("%s Tool" % PKG_NAME, tools=tools,
                   product_name=PKG_NAME,
                   icon="tool.gif",
                   ).initialize(context)
