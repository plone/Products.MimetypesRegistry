import mtr_mimetypes
import py_mimetypes
import magic

from mtr_mimetypes import *

def initialize(registry):
    mtr_mimetypes.initialize(registry)
    py_mimetypes.initialize(registry)
