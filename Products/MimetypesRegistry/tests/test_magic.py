import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Testing import ZopeTestCase
from Products.Archetypes.tests.common import *

from Products.MimetypesRegistry.mime_types.magic import guessMime
from utils import input_file_path

samplefiles = [
    ('OOoWriter', 'application/vnd.sun.xml.writer'),
    ('sxw-ooo-trolltech', 'application/vnd.sun.xml.writer'), # file from limi
    ('simplezip', 'application/zip'),
]

class TestGuessMagic(ArchetypesTestCase):

    def test_guessMime(self):
        for filename, expected in samplefiles:
            file = open(input_file_path(filename))
            data = file.read()
            file.close()
            got = guessMime(data)
            self.failUnlessEqual(got, expected)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestGuessMagic))
    return suite

if __name__ == '__main__':
    framework()
