import os
from Products.CMFCore.DirectoryView import addDirectoryViews, registerDirectory, \
     createDirectoryView, manage_listAvailableDirectories
from Products.CMFCore.utils import getToolByName, minimalpath
from Globals import package_home
from OFS.ObjectManager import BadRequestException

from Products.MimetypesRegistry import GLOBALS, skins_dir
from Products.MimetypesRegistry.interfaces import IMimetypesRegistry
from Acquisition import aq_base


def install(self):
    id = 'mimetypes_registry'
    if hasattr(aq_base(self), id) and not \
      IMimetypesRegistry.isImplementedBy(getattr(self, id)):
        self.manage_delObjects([id,])
    if not hasattr(self, id):
        addTool = self.manage_addProduct['MimetypesRegistry'].manage_addTool
        addTool('MimeTypes Registry')

    skinstool=getToolByName(self, 'portal_skins')

    fullProductSkinsPath = os.path.join(package_home(GLOBALS), skins_dir)
    productSkinsPath = minimalpath(fullProductSkinsPath)
    registered_directories = manage_listAvailableDirectories()
    if productSkinsPath not in registered_directories:
        registerDirectory(skins_dir, GLOBALS)
    try:
        addDirectoryViews(skinstool, skins_dir, GLOBALS)
    except BadRequestException, e:
        pass  # directory view has already been added

    files = os.listdir(fullProductSkinsPath)
    for productSkinName in files:
        if os.path.isdir(os.path.join(fullProductSkinsPath, productSkinName)) \
               and productSkinName != 'CVS':
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
