cmsplugin-googleplus
====================

Django-cms plugin for fetching Google+ activities.
You can find a `preview <https://github.com/itbabu/cmsplugin-googleplus#preview>`_ at the bottom of this README.



**Status**

Still in Beta.

.. image:: https://pypip.in/v/cmsplugin-googleplus/badge.png
        :target: https://crate.io/packages/cmsplugin-googleplus

.. image:: https://pypip.in/d/cmsplugin-googleplus/badge.png
        :target: https://crate.io/packages/cmsplugin-googleplus

.. image:: https://d2weczhvl823v0.cloudfront.net/itbabu/cmsplugin-googleplus/trend.png
        :target: https://bitdeli.com/free


**Continuous Integration**


.. image:: https://secure.travis-ci.org/itbabu/cmsplugin-googleplus.png?branch=master
    :target: http://travis-ci.org/#!/itbabu/cmsplugin-googleplus?branch=master

.. image:: https://coveralls.io/repos/itbabu/cmsplugin-googleplus/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/itbabu/cmsplugin-googleplus?branch=master


Install
-------

1. Install these packages and their requirements:

**NOTE**: Django 1.6.x is supported only with Django-cms 3.x

* `Django==1.4 <https://pypi.python.org/pypi/Django>`_
* `django-cms>=2.4 <https://pypi.python.org/pypi/django-cms>`_
* `google-api-python-client - 1.2 <https://pypi.python.org/pypi/google-api-python-client>`_
* `python-dateutil - 2.1 <https://pypi.python.org/pypi/python-dateutil>`_


2. Install `cmsplugin-googleplus <https://github.com/itbabu/cmsplugin-googleplus>`_ in your environment.

Configure
---------

1. `Configure django-cms <http://django-cms.readthedocs.org/en/latest/getting_started/tutorial.html#configuration-and-setup>`_
2. Add ``cmsplugin_googleplus`` to the ``INSTALLED_APPS`` list in your project's ``settings.py``.
3. Go to the `google apis console <https://code.google.com/apis/console>`_ and create a new project (a google account is required)
4. Select *Services* and activate *Google+ API*
5. Select *API Access* and get the *API key*
6. Add the *API key* to your ``settings.py``::

        GOOGLEPLUS_PLUGIN_DEVELOPER_KEY = '<your_api_key>'

Run
---

Fresh install
^^^^^^^^^^^^^

::

    python manage.py syncdb --all
    python manage.py migrate --fake

The first command will prompt you to create a super user. Choose ‘yes’ and enter appropriate values.

Upgrade
^^^^^^^
::

    python manage.py syncdb
    python manage.py migrate


How to use it
-------------

An `activity <https://developers.google.com/+/api/latest/activities>`_ is a note that a user posts to their stream.
You can `list <https://developers.google.com/+/api/latest/activities/list>`_ a collection of activities
from one user or you can list a collection of activities
as result of a `search <https://developers.google.com/+/api/latest/activities/search>`_.

Template
--------

This plugin has an example template that uses `Twitter Bootstrap 3 <http://getbootstrap.com/>`_.
You can use it as skeleton for you templates.

Create your template and inside ``settings.py`` add::


    GOOGLEPLUS_PLUGIN_TEMPLATES = (
        ('cmsplugin_googleplus/twitter_bootstrap.html',
         _('Example Template using Twitter Bootstrap')),
        ('path/to/my/template',
         _('My beautiful template'))
    )

Cache
-----

The activities are cached so you need to:

1. `Set up your cache system <https://docs.djangoproject.com/en/dev/topics/cache/#setting-up-the-cache>`_
2. (Optional) Decide the activities cache duration. Default is 5 minutes.
   Inside ``settings.py`` add::

       GOOGLEPLUS_PLUGIN_CACHE_DURATION = <custom_cache_duration>

The actual 'Courtesy Limit' for the Google+ API is 10,000 requests/day

Translation
-----------
For translators I've set up a `Transifex account <https://www.transifex.com/projects/p/cmsplugin-googleplus/>`_
where you can add languages and translate the .po

Tests
-----

Requirements
^^^^^^^^^^^^
* `mock - 1.0.1 <https://pypi.python.org/pypi/mock>`_
* `django-nose - 1.2 <https://pypi.python.org/pypi/django-nose>`_
* `coverage - 3.7 <https://pypi.python.org/pypi/coverage>`_

Run the test with coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $ coverage run runtests.py && coverage report -m


Preview
-------

This is how the plugin looks with the example template.

.. image:: https://raw.github.com/itbabu/cmsplugin-googleplus/master/cmsplugin_googleplus/docs/images/cmsplugin-googleplus-preview.png


Have Fun!

Marco
