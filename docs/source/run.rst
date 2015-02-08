Run
===

Django 1.7
----------

::

    python manage.py migrate

Django 1.4 and Django 1.6
-------------------------

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


