from os.path import dirname, join, exists
from interfaces import IMimetype
from common import HAS_ZOPE, MimeTypeException

class Mimetype:
    __implements__ = (IMimetype,)

    def __init__(self, name='', mimetypes=None, extensions=None, binary=None,
                 icon_path=''):
        if name:
            self.__name__ = self.id = name
        if mimetypes is not None:
            self.mimetypes = mimetypes
        if extensions is not None:
            self.extensions = extensions
        if binary is not None:
            self.binary = binary
        self.icon_path = icon_path or guess_icon_path(self)

    def __str__(self):
        return self.normalized()

    def __repr__(self):
        return "<mimetype %s>" % self.mimetypes[0]

    def __cmp__(self, other):
        try:
            if isinstance(other, mimetype):
                other = other.normalized()
        except:
            pass
        return not (other in self.mimetypes)

    def __hash__(self):
        return hash(self.name())

    def name(self):
        """ The name of this object """
        return self.__name__

    def major(self):
        """ return the major part of the RFC-2046 name for this mime type """
        return self.normalized().split('/', 1)[0]

    def minor(self):
        """ return the minor part of the RFC-2046 name for this mime type """
        return self.normalized().split('/', 1)[1]

    def normalized(self):
        """ return the main RFC-2046 name for this mime type

        e.g. if this object has names ('text/restructured', 'text-x-rst')
        then self.normalized() will always return the first form.
        """
        return self.mimetypes[0]




ICONS_DIR = join(dirname(__file__), 'skins', 'mimetypes_icons')

def guess_icon_path(mimetype, icons_dir=ICONS_DIR, icon_ext='png'):
    if mimetype.extensions:
        for ext in mimetype.extensions:
            icon_path = '%s.%s' % (ext, icon_ext)
            if exists(join(icons_dir, icon_path)):
                return icon_path
    icon_path = '%s.png' % mimetype.major()
    if exists(join(icons_dir, icon_path)):
        return icon_path
    return 'unknown.png'

# make mimetype zope aware on zope platforms
if HAS_ZOPE:
    from zope.MimeTypeItem import MimeTypeItem
else:
    MimeTypeItem = Mimetype
