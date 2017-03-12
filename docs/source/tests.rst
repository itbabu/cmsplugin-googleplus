Tests
=====

Requirements
------------
* `mock - 2.0.0 <https://pypi.python.org/pypi/mock>`_
* `django-nose - 1.4.4 <https://pypi.python.org/pypi/django-nose>`_
* `coverage - 4.3.4 <https://pypi.python.org/pypi/coverage>`_

Run tests with coverage
-----------------------
::

    $ coverage run runtests.py && coverage report -m

It's possible to run against multiple environments with tox.

::

    $ pip install tox

    $ tox
