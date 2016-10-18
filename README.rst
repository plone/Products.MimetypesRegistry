==================
Mimetypes Registry
==================

Provide a registry of mimetypes, accessible via the ``mimetypes_registry`` tool.


Upgrade from older versions
===========================

If you want to use the updated mimetypes registry database from the version after 2.0.6 and you don't have important customizations you need to keep,
just delete the old ``mimetypes_registry`` tool from ZMI and import all steps from the ``MimetypesRegistry`` profile.


How to update the mimetypes registry from freedesktop.org
=========================================================

1) Download the latest release from freesdesktops org `shared mime info project page <https://freedesktop.org/wiki/Software/shared-mime-info/>`_.

2) Unpack the tarball

3) Copy the ``freedesktop.org.xml`` file to Products.MimetypesRegistry's
   ``mime_types`` folder.

4) Add a note to the change log ``CHANGES.rst``.

5) Push to a branch and create a pull request.


Authors
=======

- Benjamin Saller <bcsaller@yahoo.com>
- Sidnei da Silva  <sidnei@x3ng.com>
- Sylvain Thenault <sylvain.thenault@logilab.fr>
- Christian Heimes <tiran@cheimes.de>

Credits
=======

Mimetypes registry information from freedesktop.org.

Icons from:

  * Plone: http://plone.org
  * Tango: http://tango.freedesktop.org
  * FamFamFam: http://www.famfamfam.com

