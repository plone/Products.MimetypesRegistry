from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem, guess_icon_path
from Products.MimetypesRegistry.common import MimeTypeException

import mimetypes as pymimetypes

# don't register the mimetype from python mimetypes if matching on of this
# extensions.
skip_extensions = (
    )

def initialize(registry):
    #Find things that are not in the specially registered mimetypes
    #and add them using some default policy, none of these will impl
    #iclassifier
    for ext, mt in pymimetypes.types_map.items():
        if ext[0] == '.':
            ext = ext[1:]
        
        if registry.lookupExtension(ext):
            continue
        if ext in skip_extensions:
            continue

        try:
            mto =  registry.lookup(mt)
        except MimeTypeException:
            # malformed MIME type
            continue
        if mto:
            mto = mto[0]
            if not ext in mto.extensions:
                registry.register_extension(ext, mto)
                mto.extensions += (ext, )
                # here we guess icon path again, to find icon match the new ext
                mto.icon_path = guess_icon_path(mto)
            continue
        isBin = mt.split('/', 1)[0] != "text"
        registry.register(MimeTypeItem(mt, (mt,), (ext,), isBin))
