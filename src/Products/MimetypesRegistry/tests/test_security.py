from AccessControl.ZopeGuards import guarded_getattr
from AccessControl.ZopeGuards import guarded_import

import unittest


class TestCommonModuleSecurity(unittest.TestCase):
    def setUp(self):
        import Products.MimetypesRegistry  # noqa: F401

        self.module = guarded_import(
            "Products.MimetypesRegistry.common", fromlist=["MimeTypeException"]
        )

    def test_mimetype_exception_is_public(self):
        self.assertIsNotNone(guarded_getattr(self.module, "MimeTypeException"))

    def test_other_names_are_not_public(self):
        # names imported by the module must not leak to restricted code
        self.assertRaises(Exception, guarded_getattr, self.module, "zope")
