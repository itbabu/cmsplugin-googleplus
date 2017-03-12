from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from dateutil.parser import parse
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _

from .conf import GOOGLEPLUS_PLUGIN_CACHE_DURATION
from .googleplus import GooglePlusAPI
from .models import GooglePlusActivities


class GooglePlusActivitiesPlugin(CMSPluginBase):
    """
    Plugin for including Google+ activities
    """
    model = GooglePlusActivities
    name = _("Google Plus Activity Feed")
    fieldsets = (
        (_('Settings'), {
            'fields': ('google_api_key', )
        }),
        (_('Layout'), {
            'fields': ('render_template', 'items', 'truncate_chars')
        }),
        (_('Activity List'), {
            'description': _('List of the activities in the specified '
                             'collection for a particular user.'),
            'fields': ('google_user',)
        }),
        (_('Activity Search'), {
            'description': _('Search public activities. '
                             'These fields are ignored if the "Google+ '
                             'User Id" is filled.'),
            'fields': ('query', 'preferred_language', 'order_by')
        }),
    )

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        activity_list, alert_msg = self.get_latest_activities(instance) \
            if instance.google_user else self.get_search_activities(instance)
        context['activity_list'] = self.parse_datetime(activity_list)
        context['alert_message'] = alert_msg

        return context

    def get_render_template(self, context, instance, placeholder):
        return instance.render_template

    def get_latest_activities(self, instance):
        """
        :param instance: the GooglePlusActivities instance
        :type instance: GooglePlusActivities
        :returns: list of dictionaries -- the recent activities:
            https://developers.google.com/+/api/latest/activities
            and an alert if any.

        Note: Activities are returned from the activities.list method in the
        same order that they are displayed on the google+ page. This means that
         while the first pages contain newer activities, older activities may
        be bumped up. See `this open ticket
        <https://code.google.com/p/google-plus-platform/issues/detail?id=63>`_

        """
        key_name = instance.get_cache_key(instance.pk)
        activity_list = cache.get(key_name, None)
        alert_msg = ''
        if not activity_list:
            googleplus_api = GooglePlusAPI(
                developer_key=instance.google_api_key)
            activity_list, alert_msg = googleplus_api.get_user_activity_list(
                user_id=instance.google_user, results=instance.items)
            if not alert_msg:
                cache.set(key_name, activity_list, GOOGLEPLUS_PLUGIN_CACHE_DURATION)
        return activity_list, alert_msg

    def get_search_activities(self, instance):
        key_name = instance.get_cache_key(instance.pk)
        activity_list = cache.get(key_name, None)
        alert_msg = ''
        if not activity_list:
            googleplus_api = GooglePlusAPI(
                developer_key=instance.google_api_key)
            activity_list, alert_msg = googleplus_api.get_search_activity_list(
                query=instance.query,
                preferred_language=instance.preferred_language,
                order_by=instance.order_by,
                results=instance.items)
            if not alert_msg:
                cache.set(key_name, activity_list, GOOGLEPLUS_PLUGIN_CACHE_DURATION)
        return activity_list, alert_msg

    def parse_datetime(self, activity_list):
        """
        Cleans up the activities given by the api:
        Google+ API uses RFC3339 format for dates like published date of an
        activity.
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
