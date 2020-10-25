# to keep existing imports intact, we have to keep this file here

def guessMime(data):
    # XXX: this import is a workaround, we cannot import magic directly as this file is already named that way.
    from Products.MimetypesRegistry import magic
    return magic.from_buffer(data, mime=True)
