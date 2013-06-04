CMS Plugin Google Map
====================

An app for integrating a google map in your cms layout.

Prerequisites
-------------

You will need to have the following packages installed:

* Django
* django-cms
* Pillow
* South


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-googlemap

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-googlemap.git#egg=cmsplugin_googlemap

Add ``cmsplugin_googlemap`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_googlemap',
    )

Run the South migrations::

    ./manage.py migrate cmsplugin_googlemap


Usage
-----

TODO: Describe usage

Roadmap
-------

Check the issue tracker on github for milestones and features to come.
