==================
Mimetypes Registry
==================

Provide a registry of mimetypes, accessible via the ``mimetypes_registry``
tool. 


How to update the mimetypes registry from freedesktop.org
=========================================================

1) Clone the ``shared-mime-info`` repository from freedesktop.org::

    $ git clone git://anongit.freedesktop.org/xdg/shared-mime-info

2) Build it::

    $ cd shared-mime-info
    $ ./autogen.sh
    $ ./configure 
    $ make

3) Copy the ``freedesktop.org.xml`` file to Products.MimetypesRegistry's
   ``mime_type`` folder.


Authors
=======

Benjamin Saller <bcsaller@yahoo.com>
Sidnei da Silva  <sidnei@x3ng.com>
Sylvain Thenault <sylvain.thenault@logilab.fr>
Christian Heimes <tiran@cheimes.de>

Credits
=======

Mimetypes registry information from freedesktop.org.

Icons from:

  * Plone: http://plone.org
  * Tango: http://tango.freedesktop.org
  * FamFamFam: http://www.famfamfam.com

