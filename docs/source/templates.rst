Templates
=========

This plugin has a template that uses `Material Design for Bootstrap <http://fezvrasta.github.io/bootstrap-material-design//>`_ .

You can use it as example skeleton for your templates.

As quickstart you can use a CDN for the related css::

    <!-- Material Design fonts -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" type="text/css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.4/css/bootstrap.min.css">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-material-design/0.5.2/css/bootstrap-material-design.min.css">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-material-design/0.5.2/css/ripples.min.css">

Custom Template
---------------

Create your template and inside ``settings.py`` add::

    GOOGLEPLUS_PLUGIN_TEMPLATES = (
        ('cmsplugin_googleplus/twitter_bootstrap.html',
         _('Example Template using Twitter Bootstrap')),
        ('path/to/my/template',
         _('My beautiful template'))
    )
