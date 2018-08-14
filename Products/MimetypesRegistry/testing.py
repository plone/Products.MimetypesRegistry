# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import Products.MimetypesRegistry


class ProductsMimetypesregistryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=Products.MimetypesRegistry)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'Products.MimetypesRegistry:MimetypesRegistry')


PRODUCTS_MIMETYPESREGISTRY_FIXTURE = ProductsMimetypesregistryLayer()


PRODUCTS_MIMETYPESREGISTRY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODUCTS_MIMETYPESREGISTRY_FIXTURE,),
    name='ProductsMimetypesregistryLayer:IntegrationTesting',
)
