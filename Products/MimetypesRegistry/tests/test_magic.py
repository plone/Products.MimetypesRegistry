# -*- coding: utf-8 -*-
from Products.MimetypesRegistry.tests.utils import input_file_path
from Products.CMFCore.utils import getToolByName
from Products.MimetypesRegistry.mime_types.magic import guessMime
from Products.MimetypesRegistry.testing import PRODUCTS_MIMETYPESREGISTRY_INTEGRATION_TESTING
from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem

import unittest

# sample files with alternative mimetypes (depending on OS)
samplefiles = [
    ('LibreOfficeWriter.odt', 'application/vnd.oasis.opendocument.text'),
    ('LibreOfficeCalc.ods', 'application/vnd.oasis.opendocument.spreadsheet'),
#    ('sxw-ooo-trolltech', 'application/vnd.sun.xml.writer'),  # file from limi
    ('simplezip', 'application/zip'),
    ('audio.m4a', ('audio/x-m4a', 'audio/m4a', 'audio/mp4')),
    ('audio.mp3', 'audio/mpeg'),
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

            if not isinstance(expected, tuple):
                expected = (expected,)

            # use method direct
            got = guessMime(data)
            self.assertIn(got, expected)

            # use mtr-tool
            got_from_tool = self.registry.classify(data)
            self.assertTrue(isinstance(got_from_tool, MimeTypeItem))
            self.assertIn(str(got_from_tool), expected)

            # now cut it to the first 8k if greater
            if len(data) > 8192:
                data = data[:8192]
                got_cutted = self.registry.classify(data)
                self.assertTrue(isinstance(got_from_tool, MimeTypeItem))
                self.assertIn(str(got_cutted), expected)
