from unittest  import TestCase, TestSuite, main, makeSuite

import sys, os
import re

try:
    import Zope # Sigh, make product initialization happen
    HAS_ZOPE = 1
    Zope.startup()
except ImportError:
    HAS_ZOPE = 0
except AttributeError: # Zope > 2.6
    pass

MODULE_NAME = 'Products.PortalTransforms.tests'

from Products.PortalTransforms.chain import chain
from Products.PortalTransforms.interfaces import *

from Products.PortalTransforms.MimeTypesTool import MimeTypesTool
from Products.PortalTransforms.TransformTool import TransformTool

mt_registry = MimeTypesTool()
transformer = TransformTool()
transformer.mimetypes_registry = mt_registry
from Products.PortalTransforms import transforms
transforms.initialize(transformer)
