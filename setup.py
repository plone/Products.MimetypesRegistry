from pathlib import Path
from setuptools import setup


version = "4.0.0a1.dev0"

long_description = (
    f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}"
)

setup(
    name="Products.MimetypesRegistry",
    version=version,
    description="MIME type handling for Zope",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope :: 5",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Zope mimetype registry",
    author="Benjamin Saller",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/Products.MimetypesRegistry",
    include_package_data=True,
    license="GPL",
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "Products.CMFCore",
        'pywin32 ; platform_system=="Windows"',
        "Zope",
    ],
    extras_require=dict(
        test=[
            "plone.app.contenttypes[test]",
            "plone.app.testing",
        ]
    ),
)
