
modname = 'MimetypesRegistry'
version = '1.3.0-3'
numversion = (1, 3, 0, 3)
at_versions = ('1.3.0-beta3', '1.3.0-beta4', )

license = 'BSD like'
license_text = open('LICENSE.txt').read()
copyright = '''Copyright (c) 2003 LOGILAB S.A. (Paris, FRANCE)'''

author = "Archetypes developpement team"
author_email = "archetypes-devel@lists.sourceforge.net"

short_desc = "MIME types registry for the CMF"
long_desc = """This package provides a new CMF tools in order to
make MIME types guessings. You will find more info in the package's
README and docs directory.
.
It's part of the Archetypes project, but the only requirement to use it
is to have a CMF based site. If you are using Archetypes, this package
replaces the transform package.
.
Notice this package can also be used as a standalone Python package. If
you've downloaded the Python distribution, you can't make it a Zope
product since Zope files have been removed from this distribution.
"""

web = "http://www.sourceforge.net/projects/archetypes"
ftp = ""
mailing_list = "archetypes-devel@lists.sourceforge.net"

debian_name = "zope-cmfmtr"
debian_maintainer = "Christian Heimes"
debian_maintainer_email = "heimes@faho.rwth-aachen.de"
debian_handler = "zope"
