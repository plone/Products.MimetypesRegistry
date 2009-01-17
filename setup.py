from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='Products.MimetypesRegistry',
      version=version,
      description="MIME type handling for Zope",
      long_description=open("README.txt").read() + "\n" + \
              open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        ],
      keywords='Zope catalog index',
      author='Benjamin Saller',
      author_email='plone-developers@lists.sourceforge.net',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.Archetypes',
        ]
      ),
      install_requires=[
          'setuptools',
          'zope.contenttype',
          'zope.interface',
          'Products.CMFCore',
          'Acquisition',
          'ZODB3',
          'Zope2',
      ],
      )
