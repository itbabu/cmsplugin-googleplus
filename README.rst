cmsplugin-googleplus
====================

Django-cms plugin for fetching Google+ activities

Still in Alpha.

Continuous Integration:
-----------------------

.. image:: https://secure.travis-ci.org/itbabu/cmsplugin-googleplus.png?branch=master
    :target: http://travis-ci.org/#!/itbabu/cmsplugin-googleplus?branch=master

.. image:: https://coveralls.io/repos/itbabu/cmsplugin-googleplus/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/itbabu/cmsplugin-googleplus?branch=master


Install
-------

1. Install these packages and their requirements:

    * `django-cms <https://pypi.python.org/pypi/django-cms>`_
    * `Django>=1.4 <https://pypi.python.org/pypi/Django>`_
    * `google-api-python-client - 1.2 <https://pypi.python.org/pypi/google-api-python-client>`_
    * `python-dateutil - 2.1 <https://pypi.python.org/pypi/python-dateutil>`_


2. Install `cmsplugin-googleplus <https://github.com/itbabu/cmsplugin-googleplus>`_ in your environment.

Configure
---------

1. `Configure django-cms <http://django-cms.readthedocs.org/en/latest/getting_started/tutorial.html#configuration-and-setup>`_
2. Add cmsplugin-googleplus to the INSTALLED_APPS** list in your project's ``settings.py`` and run the syncdb command on your manage.py.
3. Go to the `google apis console <https://code.google.com/apis/console>`_ and create a new project (a google account is required)
4. Select *Services* and activate *Google+ API*
5. Select *Services* and get the *API key*
6. Add the *API key* to your ``settings.py``::

        ...
        GOOGLEPLUS_PLUGIN_DEVELOPER_KEY = <ypur api key>

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

Tests
-----

Requirements
^^^^^^^^^^^^
* mock - 1.0.1
* django-nose - 1.2
* coverage - 3.6

Run the test with coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $ coverage run runtests.py && coverage report -m
