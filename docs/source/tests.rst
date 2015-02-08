Tests
=====

Requirements
------------
* `mock - 1.0.1 <https://pypi.python.org/pypi/mock>`_
* `django-nose - 1.2 <https://pypi.python.org/pypi/django-nose>`_
* `coverage - 3.7 <https://pypi.python.org/pypi/coverage>`_

Run tests with coverage
-----------------------
::

    $ coverage run runtests.py && coverage report -m

It's possible to run against multiple environments with tox.

::

    $ pip install tox

    $ tox
