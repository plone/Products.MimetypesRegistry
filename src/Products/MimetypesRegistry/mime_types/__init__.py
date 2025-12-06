from . import mtr_mimetypes
from . import py_mimetypes
from . import smi_mimetypes
from . import suppl_mimetypes
from .mtr_mimetypes import *  # noqa: F401,F403

import magic


def initialize(registry):
    smi_mimetypes.initialize(registry)
    mtr_mimetypes.initialize(registry)
    suppl_mimetypes.initialize(registry)
    py_mimetypes.initialize(registry)


def guessMime(data):
    return magic.from_buffer(data, mime=True)
