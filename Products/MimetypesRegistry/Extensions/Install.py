import os
from zope.component import getSiteManager
from zope.component import getUtility

from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.interfaces import ISkinsTool
from Globals import package_home
from OFS.ObjectManager import BadRequestException

from Products.MimetypesRegistry import GLOBALS, skins_dir
from Products.MimetypesRegistry.interfaces import IMimetypesRegistry
from Products.MimetypesRegistry.interfaces import IMimetypesRegistryTool
from Acquisition import aq_base
from StringIO import StringIO

def install(self):
    out = StringIO()
    id = 'mimetypes_registry'
    if hasattr(aq_base(self), id):
        mtr = getattr(self, id)
        if not IMimetypesRegistry.isImplementedBy(mtr) or \
          not getattr(aq_base(mtr), '_new_style_mtr', None) == 1:
            print >>out, 'Removing old mimetypes registry tool'
            self.manage_delObjects([id,])
    if not hasattr(self, id):
        addTool = self.manage_addProduct['MimetypesRegistry'].manage_addTool
        addTool('MimeTypes Registry')
        mtr = getattr(self, id)
        sm = getSiteManager()
        sm.registerUtility(mtr, IMimetypesRegistryTool)
        print >>out, 'Installing mimetypes registry tool'

    skinstool = getUtility(ISkinsTool)
    fullProductSkinsPath = os.path.join(package_home(GLOBALS), skins_dir)
    try:
        addDirectoryViews(skinstool, 'skins', GLOBALS)
    except BadRequestException, e:
        pass  # directory view has already been added

    files = os.listdir(fullProductSkinsPath)
    for productSkinName in files:
        # skip directories with a dot or special dirs
        # or maybe just startswith('.')?
        if '.' in productSkinName or productSkinName in ('CVS', '_svn', '{arch}'):
            continue
        if os.path.isdir(os.path.join(fullProductSkinsPath, productSkinName)):
            for skinName in skinstool.getSkinSelections():
                path = skinstool.getSkinPath(skinName)
                path = [i.strip() for i in  path.split(',')]
                try:
                    if productSkinName not in path:
                        path.insert(path.index('custom') +1, productSkinName)
                except ValueError:
                    if productSkinName not in path:
                        path.append(productSkinName)
                path = ','.join(path)
                skinstool.addSkinSelection(skinName, path)

    return out.getvalue()

def fixUpSMIGlobs(self):
    from Products.MimetypesRegistry.mime_types import smi_mimetypes
    from Products.Archetypes.debug import log
    mtr = getUtility(IMimetypesRegistryTool)
    smi_mimetypes.initialize(mtr)

    # Now comes the fun part. For every glob, lookup a extension
    # matching the glob and unregister it.
    for glob in mtr.globs.keys():
        if mtr.extensions.has_key(glob):
            log('Found glob %s in extensions registry, removing.' % glob)
            mti = mtr.extensions[glob]
            del mtr.extensions[glob]
            if glob in mti.extensions:
                log('Found glob %s in mimetype %s extensions, '
                    'removing.' % (glob, mti))
                exts = list(mti.extensions)
                exts.remove(glob)
                mti.extensions = tuple(exts)
                mtr.register(mti)
