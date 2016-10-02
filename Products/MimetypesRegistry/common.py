# -*- coding: utf-8 -*-
import zope.deferredimport
zope.deferredimport.initialize()

zope.deferredimport.deprecated(
    "Import from Products.MimetypesRegistry.interfaces instead",
    MimeTypeException='Products.MimetypesRegistry.interfaces:'
                      'MimeTypeException',
)
