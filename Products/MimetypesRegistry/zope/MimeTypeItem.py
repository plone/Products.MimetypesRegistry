from Acquisition import Implicit
from OFS.SimpleItem import Item
from AccessControl import ClassSecurityInfo
from Globals import Persistent, InitializeClass
from Products.CMFCore  import CMFCorePermissions
from Products.MimetypesRegistry.interfaces import IMimetype
from Products.MimetypesRegistry.MimeTypeItem import Mimetype


class MimeTypeItem(Mimetype, Persistent, Implicit, Item):
    """ A mimetype object to be managed inside the mimetypes tool """

    security = ClassSecurityInfo()
    __implements__ = (IMimetype,)

    security.declarePublic('name')
    security.declarePublic('major')
    security.declarePublic('minor')
    security.declarePublic('normalized')

    security.declareProtected(CMFCorePermissions.ManagePortal, 'edit')
    def edit(self, name, mimetypes, extensions, icon_path, binary=0,
             REQUEST=None):
        """edit this mime type"""
        # if mimetypes and extensions are string instead of lists, split them on new lines
        if type(mimetypes) in (type(''), type(u'')):
            mimetypes = [mts.strip() for mts in mimetypes.split('\n') if mts.strip()]
        if type(extensions) in (type(''), type(u'')):
            extensions = [mts.strip() for mts in extensions.split('\n') if mts.strip()]
        self.__name__ = self.id = name
        self.mimetypes = mimetypes
        self.extensions = extensions
        self.binary = binary
        self.icon_path = icon_path
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()+'/manage_main')

InitializeClass(MimeTypeItem)
