import mtr_mimetypes
import py_mimetypes
import magic

from mtr_mimetypes import text_plain, text_pre_plain, text_structured, \
    text_rest, text_python, application_rtf, application_msword, text_xml

# XXX backward compatibility trick
# Set Products.PortalTransforms.mime_types as alias for
# Products.MimetypesRegistry.mime_types because instances of BaseUnit are
# having a reference to it
import sys
this_module = sys.modules[__name__]
sys.modules['Products.PortalTransforms.mime_types'] = this_module

def initialize(registry):
    mtr_mimetypes.initialize(registry)
    py_mimetypes.initialize(registry)

