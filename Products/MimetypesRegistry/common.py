# -*- coding: utf-8 -*-
from AccessControl import ModuleSecurityInfo

import logging
import os.path

# directory where template for the ZMI are located
_www = os.path.join(os.path.dirname(__file__), 'www')

security = ModuleSecurityInfo()
security.declarePrivate('logging')
security.declarePrivate('os')
security.declarePrivate('time')

logger = logging.getLogger('MimetypesRegistry')


def log(msg, severity=logging.INFO, id='MimetypesRegistry'):
    logger.log(severity, msg)


class MimeTypeException(Exception):
    pass
