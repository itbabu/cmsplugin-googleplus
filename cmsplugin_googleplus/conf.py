from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

DEFAULT_PLUGIN_TEMPLATES = (
    ('cmsplugin_googleplus/twitter_bootstrap.html',
     _('Example Template using Twitter Bootstrap')),
)

GOOGLEPLUS_PLUGIN_CACHE_DURATION = getattr(
    settings, 'GOOGLEPLUS_PLUGIN_CACHE_DURATION', 60*5)
GOOGLEPLUS_PLUGIN_TEMPLATES = getattr(
    settings, 'GOOGLEPLUS_PLUGIN_TEMPLATES', DEFAULT_PLUGIN_TEMPLATES)
