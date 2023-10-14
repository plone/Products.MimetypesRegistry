from Products.CMFCore.utils import getToolByName
from Products.MimetypesRegistry.mime_types import application_octet_stream
from Products.MimetypesRegistry.mime_types import text_plain
from Products.MimetypesRegistry.mime_types import text_xml
from Products.MimetypesRegistry.testing import (
    PRODUCTS_MIMETYPESREGISTRY_INTEGRATION_TESTING,
)
from Products.MimetypesRegistry.tests.utils import input_file_path

import os
import unittest


class TestMimeTypesclass(unittest.TestCase):
    layer = PRODUCTS_MIMETYPESREGISTRY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.registry = getToolByName(self.portal, "mimetypes_registry")

    def testClassify(self):
        reg = self.registry
        c = reg._classifiers()
        self.assertTrue(
            c[0].name().startswith("Extensible Markup Language"), c[0].name()
        )

        # Real XML
        data = "<?xml version='1.0'?><foo>bar</foo>"
        mt = reg.classify(data)
        self.assertTrue(isinstance(mt, text_xml), str(mt))

        # with leading whitespace (http://dev.plone.org/archetypes/ticket/622)
        # still valid xml
        data = " <?xml version='1.0'?><foo>bar</foo>"
        mt = reg.classify(data)
        self.assertTrue(isinstance(mt, text_xml), str(mt))

        # also #622: this is not xml
        data = "xml > plain text"
        mt = reg.classify(data)
        self.assertTrue(str(mt) != "text/xml")

        # Passed in MT
        mt = reg.classify(data, mimetype="text/plain")
        self.assertTrue(isinstance(mt, text_plain), str(mt))

        # Passed in filename
        mt = reg.classify(data, filename="test.xml")
        self.assertTrue(isinstance(mt, text_xml), str(mt))
        mt = reg.classify(data, filename="test.jpg")
        self.assertEqual(str(mt), "image/jpeg")

        # Passed in uppercase filename
        mt = reg.classify(data, filename="test.JPG")
        self.assertEqual(str(mt), "image/jpeg")

        # use xml classifier
        mt = reg.classify("<?xml ?>")
        self.assertTrue(isinstance(mt, text_xml), str(mt))

        # test no data return default
        mt = reg.classify("")
        self.assertTrue(isinstance(mt, text_plain), str(mt))
        reg.defaultMimetype = "text/xml"
        mt = reg.classify("")
        self.assertTrue(isinstance(mt, text_xml), str(mt))

        data = os.urandom(1024)
        # test unclassifiable data and no stream flag (filename)
        mt = reg.classify(data)
        self.assertTrue(isinstance(mt, application_octet_stream), str(mt))

        # test that an unknown file extension does not help classifying data
        mt = reg.classify(data, filename="xxx")
        self.assertTrue(isinstance(mt, application_octet_stream), str(mt))

    def testExtension(self):
        reg = self.registry
        data = "<foo>bar</foo>"
        mt = reg.lookupExtension(filename="test.xml")
        self.assertTrue(isinstance(mt, text_xml), str(mt))

        mt = reg.classify(data, filename="test.foo")
        self.assertTrue(isinstance(mt, text_plain), str(mt))

        mt = reg.classify(data, filename="test.tgz")
        self.assertEqual(str(mt), "application/x-tar")

        mt = reg.classify(data, filename="test.tar.gz")
        self.assertEqual(str(mt), "application/x-tar")

        mt = reg.classify(data, filename="test.pdf.gz")
        self.assertEqual(str(mt), "application/pdf")

    def testFDOGlobs(self):
        # The mime types here might only match if they match a glob on
        # the freedesktop.org registry.
        data = ""
        reg = self.registry

        mt = reg.classify(data, filename="test.ogg")
        self.assertEqual(str(mt), "audio/ogg")

        mt = reg.classify(data, filename="test.docx")
        self.assertEqual(
            str(mt),
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )  # noqa

        mt = reg.classify(data, filename="test.anim1")
        self.assertEqual(str(mt), "video/x-anim")

        mt = reg.classify(data, filename="test.ini~")
        self.assertEqual(str(mt), "application/x-trash")

        mt = reg.classify(data, filename="test.ini%")
        self.assertEqual(str(mt), "application/x-trash")

        mt = reg.classify(data, filename="test.ini.bak")
        self.assertEqual(str(mt), "application/x-trash")

        # TODO: wrongly recognized as text/plain...
        # mt = reg.classify(data, filename="test.f90")
        # self.assertEqual(str(mt), 'text/x-fortran')

        mt = reg.classify(data, filename="test.f95")
        self.assertEqual(str(mt), "text/x-fortran")

        mt = reg.classify(data, filename="makefile")
        self.assertEqual(str(mt), "text/x-makefile")

        # Updated freedesktop.org.xml changed "Makefile" glob to "Makefile."
        # See: https://bugs.freedesktop.org/show_bug.cgi?id=88625
        # mt = reg.classify(data, filename="Makefile")
        # self.assertEqual(str(mt), 'text/x-makefile')

        mt = reg.classify(data, filename="AUTHORS")
        self.assertEqual(str(mt), "text/x-authors")

        mt = reg.classify(data, filename="INSTALL")
        self.assertTrue(
            str(mt) in ["text/x-install", "application/x-install-instructions"]
        )

    def testLookup(self):
        reg = self.registry
        mt = reg.lookup("text/plain")
        self.assertTrue(isinstance(mt[0], text_plain), str(mt[0]))

        # Test lookup of aliases in SMI database (see smi_mimetypes)
        mt1 = reg.lookup("application/vnd.wordperfect")
        mt2 = reg.lookup("application/wordperfect")
        self.assertEqual(mt1, mt2)

        mt = reg.lookup("text/notexistent")
        self.assertEqual(mt, ())

    def testAdaptMt(self):
        data, filename, mt = self.registry("bar", mimetype="text/xml")
        # this test that data has been adapted and file seeked to 0
        self.assertEqual(data, "bar")
        self.assertEqual(filename, None)
        self.assertTrue(isinstance(mt, text_xml), str(mt))

    def testAdaptFile(self):
        file = open(input_file_path("rest1.rst"))
        data, filename, mt = self.registry(file)
        # this test that data has been adapted and file seeked to 0
        self.assertEqual(data, file.read())
        file.close()
        self.assertEqual(filename, "rest1.rst")
        self.assertEqual(str(mt), "text/x-rst")

    def testAdaptData(self):
        data, filename, mt = self.registry("<?xml ?>")
        # this test that data has been adapted and file seeked to 0
        self.assertEqual(data, "<?xml ?>")
        self.assertEqual(filename, None)
        self.assertTrue(isinstance(mt, text_xml), str(mt))
