from pathlib import Path
from setuptools import find_packages
from setuptools import setup


version = "3.0.1.dev0"

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
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Zope mimetype registry",
    author="Benjamin Saller",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/Products.MimetypesRegistry",
    packages=find_packages(),
    namespace_packages=["Products"],
    include_package_data=True,
    license="GPL",
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "Products.CMFCore",
        "setuptools",
        'pywin32 ; platform_system=="Windows"',
    ],
    extras_require=dict(
        test=[
            "plone.app.contenttypes[test]",
            "plone.app.testing",
        ]
    ),
)
