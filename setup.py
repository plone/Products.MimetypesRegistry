# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.1.5'

setup(
    name='Products.MimetypesRegistry',
    version=version,
    description="MIME type handling for Zope",
    long_description=open("README.rst").read() + "\n" +
    open("CHANGES.rst").read(),
    classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='Zope mimetype registry',
    author='Benjamin Saller',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/Products.MimetypesRegistry',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    license='GPL',
    zip_safe=False,
    install_requires=[
        'AccessControl>=3.0.0'
        'Acquisition',
        'Products.CMFCore',
        'setuptools',
        'six',
        'zope.contenttype',
        'zope.deferredimport',
        'zope.interface',
        'Zope2',
    ],
    extras_require=dict(
        test=[
            'plone.app.testing',
        ]
    ),
)
