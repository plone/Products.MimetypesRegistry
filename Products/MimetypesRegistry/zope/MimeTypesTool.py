from OFS.Folder import Folder
from Products.CMFCore  import CMFCorePermissions
from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.TypesTool import  FactoryTypeInformation
from Products.CMFCore.utils import UniqueObject
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Globals import InitializeClass
from Acquisition import aq_parent
from AccessControl import ClassSecurityInfo

from Products.MimetypesRegistry.interfaces import ISourceAdapter, IMimetypesRegistry
from Products.MimetypesRegistry.common import log, _www
from Products.MimetypesRegistry.MimeTypesRegistry import MimeTypesRegistry
from Products.MimetypesRegistry.zope.MimeTypeItem import MimeTypeItem
from Products.MimetypesRegistry.mime_types import initialize

class MimeTypesTool(UniqueObject, ActionProviderBase, Folder, MimeTypesRegistry):
    """extend the MimeTypesRegistry of CMF compliance
    """

    __implements__ = (IMimetypesRegistry, ISourceAdapter)

    id        = 'mimetypes_registry'
    meta_type = 'MimeTypes Registry'
    isPrincipiaFolderish = 1 # Show up in the ZMI

    meta_types = all_meta_types = (
        { 'name'   : 'MimeType',
          'action' : 'manage_addMimeTypeForm'},
        )

    manage_options = (
        ( { 'label'   : 'MimeTypes',
            'action' : 'manage_main'},) +
        Folder.manage_options[2:]
        )

    manage_addMimeTypeForm = PageTemplateFile('addMimeType', _www)
    manage_main = PageTemplateFile('listMimeTypes', _www)
    manage_editMimeTypeForm = PageTemplateFile('editMimeType', _www)

    security = ClassSecurityInfo()

    security.declareProtected(CMFCorePermissions.ManagePortal, 'register')
    security.declareProtected(CMFCorePermissions.ManagePortal, 'unregister')
    security.declarePublic('mimetypes')
    security.declarePublic('list_mimetypes')
    security.declarePublic('lookup')
    security.declarePublic('lookupExtension')
    security.declarePublic('classify')

    # FIXME
    __allow_access_to_unprotected_subobjects__ = 1

    def __init__(self, fill=1):
        MimeTypesRegistry.__init__(self, fill=1)
        del self.defaultMimetype
        self.manage_addProperty('defaultMimetype', 'text/plain', 'string')
        del self.unicodePolicy
        self.manage_addProperty('unicodePolicies', 'strict ignore replace', 'tokens')
        del self.fallbackEncoding
        self.manage_addProperty('fallbackEncoding', 'latin1', 'string')
        self.manage_addProperty('unicodePolicy', 'unicodePolicies', 'selection')

    def __setstate__(self, state):
        Folder.__setstate__(self, state)
        initialize(self)

    security.declareProtected(CMFCorePermissions.ManagePortal, 'manage_delObjects')
    def manage_delObjects(self, ids, REQUEST=None):
        """ delete the selected mime types """
        for id in ids:
            self.unregister(self.lookup(id)[0])
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()+'/manage_main')

    security.declareProtected(CMFCorePermissions.ManagePortal, 'manage_addMimeType')
    def manage_addMimeType(self, id, mimetypes, extensions, icon_path, binary=0,
                           REQUEST=None):
        """add a mime type to the tool"""
        mt = MimeTypeItem(id, mimetypes, extensions, binary, icon_path)
        self.register(mt)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()+'/manage_main')


    security.declareProtected(CMFCorePermissions.ManagePortal, 'manage_editMimeType')
    def manage_editMimeType(self, name, new_name, mimetypes, extensions, icon_path, binary=0,
                            REQUEST=None):
        """edit a mime type by name"""
        mt = self.lookup(name)[0]
        self.unregister(mt)
        mt.edit(new_name, mimetypes, extensions, icon_path, binary)
        self.register(mt)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()+'/manage_main')


InitializeClass(MimeTypesTool)
