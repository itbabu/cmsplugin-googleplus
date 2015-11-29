from __future__ import unicode_literals

from cms.api import add_plugin, create_page
from cms.models import CMSPlugin

from ..conf import DEFAULT_PLUGIN_TEMPLATES
from .base import BaseGooglePlusTestCase

__all__ = [
    'GooglePlusPluginTestCase',
]


class GooglePlusPluginTestCase(BaseGooglePlusTestCase):

    def setUp(self):
        super(GooglePlusPluginTestCase, self).setUp()
        self.page = create_page("render test", "nav_playground.html", "en")
        self.ph = self.page.placeholders.get(slot="body")

    def test_plugin_user_activity_list(self):
        self.assertEqual(CMSPlugin.objects.all().count(), 0)
        add_plugin(
            self.ph, "GooglePlusActivitiesPlugin", "en",
            google_user="test",
            render_template=DEFAULT_PLUGIN_TEMPLATES[0][0])
        self.page.publish(language="en")
        self.assertEqual(CMSPlugin.objects.filter(
            placeholder__page__publisher_is_draft=False).count(), 1)
        response = self.client.get(self.page.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['activity_list']), 20)

    def test_plugin_search_activity_list(self):
        self.assertEqual(CMSPlugin.objects.all().count(), 0)
        add_plugin(
            self.ph, "GooglePlusActivitiesPlugin", "en", query="test",
            render_template=DEFAULT_PLUGIN_TEMPLATES[0][0])
        self.page.publish(language='en')
        self.assertEqual(CMSPlugin.objects.filter(
            placeholder__page__publisher_is_draft=False).count(), 1)
        response = self.client.get(self.page.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['activity_list']), 20)
