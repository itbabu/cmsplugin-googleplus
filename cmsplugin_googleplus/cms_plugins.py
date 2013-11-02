from __future__ import unicode_literals

from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _

from dateutil.parser import parse
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import GOOGLEPLUS_PLUGIN_DEVELOPER_KEY, GOOGLEPLUS_PLUGIN_CACHE_DURATION
from .googleplus import GooglePlusAPI
from .models import GooglePlusActivities


class GooglePlusActivitiesPlugin(CMSPluginBase):
    """
    Plugin for including Google+ activities
    """
    model = GooglePlusActivities
    name = _("Google Plus Activity Feed")
    fieldsets = (
        (_('Layout'), {
            'fields': ('render_template', 'items', 'truncate_chars')
        }),
        (_('Activity List'), {
            'description': _('List of the activities in the specified collection for a particular user.'),
            'fields': ('google_user',)
        }),
        (_('Activity Search'), {
            'description': _('Search public activities. '
                             'These fields are ignored if the "Google+ User Id" is filled.'),
            'fields': ('query', 'preferred_language', 'order_by')
        }),
    )

    def __init__(self, *args, **kwargs):
        super(GooglePlusActivitiesPlugin, self).__init__(*args, **kwargs)
        self.googleplus_api = GooglePlusAPI(developer_key=GOOGLEPLUS_PLUGIN_DEVELOPER_KEY)

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        activity_list = self.get_latest_activities(instance) if instance.google_user \
            else self.get_search_activities(instance)
        context['activity_list'] = self.parse_datetime(activity_list)

        return context

    def get_latest_activities(self, instance):
        """
        :param instance: the GooglePlusActivities instance
        :type instance: GooglePlusActivities
        :returns: list of dictionaries -- the recent activities: https://developers.google.com/+/api/latest/activities

        Note: Activities are returned from the activities.list method in the same order that they are displayed on
        the google+ page. This means that while the first pages contain newer activities, older activities may
        be bumped up. See `this open ticket <https://code.google.com/p/google-plus-platform/issues/detail?id=63>`_

        """
        key_name = 'google_plus_user_activities_%d' % instance.pk
        activity_list = cache.get(key_name, None)
        if not activity_list:
            activity_list = self.googleplus_api.get_user_activity_list(
                user_id=instance.google_user, results=instance.items)
            cache.set(key_name, activity_list, GOOGLEPLUS_PLUGIN_CACHE_DURATION)
        return activity_list

    def get_search_activities(self, instance):
        key_name = 'google_plus_search_activities_%d' % instance.pk
        activity_list = cache.get(key_name, None)
        if not activity_list:
            activity_list = self.googleplus_api.get_search_activity_list(
                query=instance.query, preferred_language=instance.preferred_language, order_by=instance.order_by,
                results=instance.items)
            cache.set(key_name, activity_list, GOOGLEPLUS_PLUGIN_CACHE_DURATION)
        return activity_list

    def parse_datetime(self, activity_list):
        """
        Cleans up the activities given by the api:
        Google+ API uses RFC3339 format for dates like published date of an activity.
        We need to parse these dates so they will be displayed in a nicer way.
        """
        parsed_activity_list = []
        for activity in activity_list:
            published = activity.get('published', None)
            updated = activity.get('updated', None)
            if published:
                activity['published'] = parse(published)
            if updated:
                activity['updated'] = parse(updated)
            parsed_activity_list.append(activity)
        return parsed_activity_list


plugin_pool.register_plugin(GooglePlusActivitiesPlugin)