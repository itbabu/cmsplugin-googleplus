from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from .conf import GOOGLEPLUS_PLUGIN_TEMPLATES
from .globals import GOOGLEPLUS_PLUGIN_LANGUAGE_CHOICES, GOOGLEPLUS_PLUGIN_ORDER_BY_CHOICES, RECENT


class GooglePlusActivities(CMSPlugin):
    """
    Plugin for including Google+ activities
    """
    render_template = models.CharField(_('template'), max_length=100, choices=GOOGLEPLUS_PLUGIN_TEMPLATES)
    items = models.SmallIntegerField(_('item'), default=5,
                                     validators=[MaxValueValidator(20), MinValueValidator(1)],
                                     help_text=_("Number of Google Plus activities to return. "
                                                 "From 1 to 100. Default is 10."),)
    truncate_chars = models.PositiveIntegerField(
        _('truncate chars'), default=150,
        help_text=_('Truncates the content, annotation and attachment after a certain number of characters.'))
    google_user = models.CharField(_('Google+ User Id'), blank=True,
                                   help_text=_('The ID of the user to get activities for'),
                                   max_length=75)
    query = models.CharField(
        _('search query'), max_length=250, blank=True, help_text=_('Full-text search query string.'))
    preferred_language = models.CharField(
        _('preferred language'), blank=True, max_length=10, choices=GOOGLEPLUS_PLUGIN_LANGUAGE_CHOICES,
        help_text=_('Optional. Specify the preferred language to search with.'))
    order_by = models.CharField(
        max_length=20, choices=GOOGLEPLUS_PLUGIN_ORDER_BY_CHOICES, default=RECENT, blank=True,
        help_text=_("Optional. Specifies how to order search results. 'best': Sort activities by relevance "
                    "to the user, most relevant first, 'recent': Sort activities by published date, most recent "
                    "first."))

    def __unicode__(self):
        return ('Google User id: %s' % self.google_user) if self.google_user else ('Search Query: %s' % self.query)

    def clean(self):
        if not self.google_user and not self.query:
            raise ValidationError(_('"Google+ user id" or "Search query" must be provided'))