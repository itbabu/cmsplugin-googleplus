from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .conf import GOOGLEPLUS_PLUGIN_TEMPLATES
from .globals import (
    GOOGLEPLUS_PLUGIN_LANGUAGE_CHOICES, GOOGLEPLUS_PLUGIN_ORDER_BY_CHOICES,
    RECENT)


@python_2_unicode_compatible
class GooglePlusActivities(CMSPlugin):
    """
    Plugin for including Google+ activities
    """
    render_template = models.CharField(
        _('template'), max_length=100, choices=GOOGLEPLUS_PLUGIN_TEMPLATES)
    items = models.SmallIntegerField(
        _('item'), default=5,
        validators=[MaxValueValidator(20), MinValueValidator(1)],
        help_text=_("Number of Google Plus activities to return. "
                    "From 1 to 100. Default is 10."),)
    truncate_chars = models.PositiveIntegerField(
        _('truncate chars'), default=150,
        help_text=_('Truncates the content, annotation and attachment after a '
                    'certain number of characters.'))
    google_user = models.CharField(
        _('Google+ User Id'), blank=True,
        help_text=_('The ID of the user to get activities for'),
        max_length=75)
    query = models.CharField(
        _('search query'), max_length=250, blank=True,
        help_text=_('Full-text search query string.'))
    preferred_language = models.CharField(
        _('preferred language'), blank=True,
        max_length=10, choices=GOOGLEPLUS_PLUGIN_LANGUAGE_CHOICES,
        help_text=_('Optional. Specify the preferred language to search with.')
    )
    order_by = models.CharField(
        _('order by'),
        max_length=20, choices=GOOGLEPLUS_PLUGIN_ORDER_BY_CHOICES,
        default=RECENT, blank=True,
        help_text=_("Optional. Specifies how to order search results. 'best': "
                    "Sort activities by relevance to the user, most relevant "
                    "first, 'recent': Sort activities by published date, most "
                    "recent first."))
    google_api_key = models.CharField(
        _('Google API key'),
        help_text=_('To use the Google+ API, you must register your project '
                    'on the Google Developers Console and get a Google '
                    'API key.'),
        max_length=75)

    def __str__(self):
        return ('Google User id: %s' % self.google_user) \
            if self.google_user else ('Search Query: %s' % self.query)

    def save(self, *args, **kwargs):
        """
        Save and invalidate cached activities
        """
        super(GooglePlusActivities, self).save(*args, **kwargs)
        key = self.get_cache_key()
        cache.delete(key)

    def clean(self):
        if not self.google_user and not self.query:
            raise ValidationError(
                _('"Google+ user id" or "Search query" must be provided'))

    def get_cache_key(self, search=False):
        if self.pk:
            if self.google_user:
                return 'google_plus_user_activities_%d' % self.pk
            else:
                return 'google_plus_search_activities_%d' % self.pk
        return None
