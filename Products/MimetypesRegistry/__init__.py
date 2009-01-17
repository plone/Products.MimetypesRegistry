from Products.MimetypesRegistry import MimeTypesRegistry

GLOBALS = globals()
PKG_NAME = 'MimetypesRegistry'

tools = (
    MimeTypesRegistry.MimeTypesRegistry,
    )

from Products.MimetypesRegistry import mime_types

def initialize(context):
    from Products.CMFCore import utils
    utils.ToolInit("%s Tool" % PKG_NAME, 
                   tools=tools,
                   icon="tool.gif",
                   ).initialize(context)
