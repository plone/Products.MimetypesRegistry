# -*- coding: utf-8 -*-
from .mtr_mimetypes import *

from . import mtr_mimetypes
from . import py_mimetypes
from . import smi_mimetypes
from . import suppl_mimetypes


def initialize(registry):
    smi_mimetypes.initialize(registry)
    mtr_mimetypes.initialize(registry)
    suppl_mimetypes.initialize(registry)
    py_mimetypes.initialize(registry)
