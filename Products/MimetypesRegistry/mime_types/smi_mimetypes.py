import os
from xml.dom import minidom, XML_NAMESPACE

from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem
from Products.MimetypesRegistry.common import MimeTypeException

#shared mime info name space
SMINS = 'http://www.freedesktop.org/standards/shared-mime-info'

DIR = os.path.dirname(__file__)
SMI_NAME = "freedesktop.org.xml"
SMI_FILE = os.path.join(DIR, SMI_NAME)

def readSMIFile(infofile):
    """Reads a shared mime info XML file

    Bases on the reader from kio-transforms
    Project:    Kio Transforms
    Client:	    Isia standing group
    Authors:    Joe Geldart (jgeldart) -- jgeldart@netalleynetworks.com
                Michael Zeltner (mzeltner) -- mzeltner@netalleynetworks.com
    """
    dom = minidom.parse(infofile)

    results = []

    # For each mime-type node...
    for mtype in dom.getElementsByTagName('mime-type'):
        # Get the MIME type
        type = mtype.getAttribute('type')
        children = [ c for c in mtype.childNodes if c.nodeType == c.ELEMENT_NODE ]

        # For each comment node...
        commentnodes = [ com for com in children if com.tagName == 'comment']
        comments = {}
        for com in commentnodes:
            lang = com.getAttributeNS(XML_NAMESPACE, 'lang') or 'en'
            comments[lang] = ''.join([n.nodeValue for n in com.childNodes]).strip()

        # For each glob node...
        globnodes = [ glb for glb in children if glb.tagName == 'glob']
        globs = []
        for glob in globnodes:
            globs.append(glob.getAttribute('pattern') or None)

        results.append({'type' : type,
                        'comments' : comments,
                        'globs' : globs,
                       })

    # Unlink reference cycles (for garbage collection)
    dom.unlink()

    return results

mimetypes = readSMIFile(SMI_FILE)

def initialize(registry):
    # Find things that are not in the specially registered mimetypes
    # and add them using some default policy, none of these will impl
    # iclassifier
    global mimetypes
    for res in mimetypes:
        mt = str(res['type'])

        # check the mime type
        try:
            mto =  registry.lookup(mt)
        except MimeTypeException:
            # malformed MIME type
            continue

        name = str(res['comments'].get(u'en', mt))

        # build a list of globs
        globs = []
        for glob in res['globs']:
            if registry.lookupGlob(glob):
                continue
            else:
                globs.append(glob)

        if mto:
            mto = mto[0]
            for glob in globs:
                if not glob in mto.globs:
                    registry.register_glob(glob, mto)
                mto.globs = list(mto.globs) + [glob]
        else:
            isBin = mt.split('/', 1)[0] != "text"
            mti = MimeTypeItem(name, mimetypes=(mt,), binary=isBin,
                               globs=globs)
            registry.register(mti)
