# -*- coding: utf-8 -*-
from AccessControl.SecurityInfo import allow_class
from AccessControl.SecurityInfo import allow_module
from Products.MimetypesRegistry import MimeTypesRegistry
from Products.MimetypesRegistry.common import MimeTypeException


GLOBALS = globals()
PKG_NAME = 'MimetypesRegistry'
tools = (MimeTypesRegistry.MimeTypesRegistry, )
allow_module('Products.MimetypesRegistry.common')
allow_class(MimeTypeException)


def initialize(context):
    from Products.CMFCore import utils
    utils.ToolInit(
        "%s Tool" % PKG_NAME,
        tools=tools,
        icon="tool.gif",
    ).initialize(context)
