import os
import json

from django.test import TestCase
from cms.api import create_page, add_plugin
from cms.models import CMSPlugin
from mock import patch, Mock

from ..googleplus import GooglePlusAPI

TEST_DEVELOPER_KEY = '123'
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

__all__ = [
    'GooglePlusAPITestCase',
    'GooglePlusPluginTestCase'
]


def datafile(filename):
    return os.path.join(DATA_DIR, filename)


def data_from_file(filename):
    path = os.path.join(DATA_DIR, filename)
    f = file(path, 'r')
    data = f.read()
    f.close()
    return json.loads(data)


class BaseGooglePlusTestCase(TestCase):
    def setUp(self):
        super(BaseGooglePlusTestCase, self).setUp()
        #TODO: improve this. apiclient.http.HttpMock should be used as argument in apiclient.http.HttpRequest.execute.
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.return_value": data_from_file('activities.json'),
            "activities.return_value.search.return_value.execute.return_value": data_from_file('activities.json')
        })
        self.patcher = patch("cmsplugin_googleplus.googleplus.build", return_value=mock)
        self.patcher.start()
        self.google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)

    def tearDown(self):
        self.patcher.stop()


class GooglePlusAPITestCase(BaseGooglePlusTestCase):

    def test_google_plus_api_initialization(self):
        google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
        self.assertIsNotNone(google_plus_api)
        self.assertIsInstance(google_plus_api, GooglePlusAPI)

    def test_user_activity_list_fetching(self):
        activity_list = self.google_plus_api.get_user_activity_list(user_id='test')
        self.assertEqual(len(activity_list), 20)
        self.assertEqual(activity_list[0]['actor']['displayName'], 'Google')

    def test_search_activity_list_fetching(self):
        activity_list = self.google_plus_api.get_search_activity_list(query='test')
        self.assertEqual(len(activity_list), 20)
        self.assertEqual(activity_list[0]['actor']['displayName'], 'Google')


class GooglePlusPluginTestCase(BaseGooglePlusTestCase):
    def test_plugin(self):
        page = create_page("render test", "nav_playground.html", "en")
        ph = page.placeholders.get(slot="body")
        self.assertEqual(CMSPlugin.
                         objects.all().count(), 0)
        google_plus_plugin = add_plugin(ph, "GooglePlusActivitiesPlugin", "en", google_user="test",
                                        render_template='cmsplugin_googleplus/twitter_bootstrap.html')
        page.publish()
        self.assertEqual(CMSPlugin.objects.filter(placeholder__page__publisher_is_draft=False).count(), 1)
        response = self.client.get(page.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['activity_list']), 20)




