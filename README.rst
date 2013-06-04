CMS Plugin Google Map
====================

An app for integrating a google map in your cms layout. This is an exact
copy of [django-cms googlemape](https://github.com/divio/django-cms/tree/develop/cms/plugins/googlemap).

The only difference is that all [fields](https://github.com/bitmazk/cmsplugin-googlemap/blob/master/cmsplugin_googlemap/models.py#L25)
except city are now optional.

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

If you were using the googlemap plugin that comes with django-cms you need
uninstall it first, like so::

    ./manage.py cms uninstall plugins GoogleMapPlugin
    psql -U role dbname -h localhost
    DROP TABLE cmsplugin_googlemap;

Run the South migrations::

    ./manage.py migrate cmsplugin_googlemap


Usage
-----

Simply add the plugin to your cms placeholders.

Roadmap
-------

Check the issue tracker on github for milestones and features to come.
