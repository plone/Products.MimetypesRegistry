# -*- coding: utf-8 -*-
from Products.MimetypesRegistry.tests.utils import input_file_path
from Products.CMFCore.utils import getToolByName
from Products.MimetypesRegistry.mime_types.magic import guessMime
from Products.MimetypesRegistry.testing import PRODUCTS_MIMETYPESREGISTRY_INTEGRATION_TESTING
from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem

import unittest


samplefiles = [
    ('OOoWriter', 'application/vnd.sun.xml.writer'),
    ('OOoCalc', 'application/vnd.sun.xml.calc'),
    ('sxw-ooo-trolltech', 'application/vnd.sun.xml.writer'),  # file from limi
    ('simplezip', 'application/zip'),
]


class TestGuessMagic(unittest.TestCase):

    layer = PRODUCTS_MIMETYPESREGISTRY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getToolByName(self.portal, 'mimetypes_registry')

    def test_guessMime(self):
        for filename, expected in samplefiles:
            file = open(input_file_path(filename), 'rb')
            data = file.read()
            file.close()

            # use method direct
            got = guessMime(data)
            self.assertEqual(got, expected)

            # use mtr-tool
            got_from_tool = self.registry.classify(data)
            self.assertTrue(isinstance(got_from_tool, MimeTypeItem))
            self.assertEqual(str(got_from_tool), expected)

            # now cut it to the first 8k if greater
            if len(data) > 8192:
                data = data[:8192]
                got_cutted = self.registry.classify(data)
                self.assertTrue(isinstance(got_from_tool, MimeTypeItem))
                self.assertEqual(str(got_cutted), expected)
