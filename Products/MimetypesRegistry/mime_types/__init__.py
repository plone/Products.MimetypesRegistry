import mtr_mimetypes
import py_mimetypes
import magic

def initialize(registry):
    mtr_mimetypes.initialize(registry)
    py_mimetypes.initialize(registry)

