cmsplugin-googleplus
====================

Django-cms plugin for fetching Google+ activities

Still in Pre-Alpha.

Continuous Integration:
-----------------------

.. image:: https://secure.travis-ci.org/itbabu/cmsplugin-googleplus.png?branch=master
    :target: http://travis-ci.org/#!/itbabu/cmsplugin-googleplus?branch=master

.. image:: https://coveralls.io/repos/itbabu/cmsplugin-googleplus/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/itbabu/cmsplugin-googleplus?branch=master

Requirements
------------
* `google-api-python-client - 1.2 <https://pypi.python.org/pypi/google-api-python-client>`_
* `python-dateutil - 2.1 <https://pypi.python.org/pypi/python-dateutil>`_


Tests
-----

Requirements
^^^^^^^^^^^^
* mock - 1.0.1
* django-nose - 1.2
* coverage - 3.6

    $ coverage run runtests.py && coverage report