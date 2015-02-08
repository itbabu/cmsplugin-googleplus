Templates
=========

This plugin has a template that uses `Twitter Bootstrap 3 <http://getbootstrap.com/>`_.

You can use it as example skeleton for your templates.

As quickstart you can use a CDN for the related css::

    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

and the related javascript::

    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>


Custom Template
---------------

Create your template and inside ``settings.py`` add::

    GOOGLEPLUS_PLUGIN_TEMPLATES = (
        ('cmsplugin_googleplus/twitter_bootstrap.html',
         _('Example Template using Twitter Bootstrap')),
        ('path/to/my/template',
         _('My beautiful template'))
    )
