__version__ = (1, 1, 0)

import common 

GLOBALS = globals()
PKG_NAME = 'MimetypesRegistry'
skins_dir = common.skins_dir

import MimeTypesTool

tools = (
    MimeTypesTool.MimeTypesTool,
    )

def initialize(context):
    from Products.CMFCore.DirectoryView import registerDirectory
    registerDirectory(skins_dir, GLOBALS)
    
    from Products.CMFCore import utils
    utils.ToolInit("%s Tool" % PKG_NAME, tools=tools,
                   product_name=PKG_NAME,
                   icon="tool.gif",
                   ).initialize(context)
