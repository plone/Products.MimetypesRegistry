__version__ = (1, 3, 1, 1)

import common 

GLOBALS = globals()
PKG_NAME = 'MimetypesRegistry'
skins_dir = common.skins_dir

import MimeTypesTool

tools = (
    MimeTypesTool.MimeTypesTool,
    )

# XXX backward compatibility tricks to make old PortalTransform based Mimetypes
# running (required)
import sys
from Products.MimetypesRegistry import mime_types
sys.modules['Products.PortalTransforms.mime_types'] = mime_types

from Products.MimetypesRegistry import MimeTypeItem
sys.modules['Products.PortalTransforms.MimeTypeItem'] = MimeTypeItem

from Products.MimetypesRegistry.zope import MimeTypeItem
sys.modules['Products.PortalTransforms.zope.MimeTypeItem'] = MimeTypeItem

def initialize(context):
    from Products.CMFCore.DirectoryView import registerDirectory
    registerDirectory(skins_dir, GLOBALS)
    
    from Products.CMFCore import utils
    utils.ToolInit("%s Tool" % PKG_NAME, tools=tools,
                   product_name=PKG_NAME,
                   icon="tool.gif",
                   ).initialize(context)
