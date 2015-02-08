Configure
=========

Google
------

1. `Configure django-cms <http://django-cms.readthedocs.org/en/latest/how_to/integrate.html>`_
2. Add ``cmsplugin_googleplus`` and ``'django.contrib.humanize'`` to the ``INSTALLED_APPS`` list in your project's ``settings.py``.
3. Go to the `google apis console <https://console.developers.google.com/project>`_ and create a new project or select an existent one (a google account is required)
4. Select *APIs* under *APIs & Auth* and activate *Google+ API*

.. image:: https://raw.github.com/itbabu/cmsplugin-googleplus/master/cmsplugin_googleplus/docs/images/google-developers-console.png

5. Select *Credentials* and *Create new Key* (Browser key)
6. Add the *API key* to your ``settings.py``::

        GOOGLEPLUS_PLUGIN_DEVELOPER_KEY = '<your_api_key>'



Cache
-----

The activities are cached so you need to:

1. `Set up your cache system <https://docs.djangoproject.com/en/dev/topics/cache/#setting-up-the-cache>`_
2. (Optional) Decide the activities cache duration. Default is 5 minutes.
   Inside ``settings.py`` add::

       GOOGLEPLUS_PLUGIN_CACHE_DURATION = <custom_cache_duration>

The actual 'Courtesy Limit' for the Google+ API is 10,000 requests/day
