
import os
import json
from django.test.utils import override_settings
from httplib2 import Response

from django.test import TestCase
from cms.api import create_page, add_plugin
from cms.models import CMSPlugin
from mock import patch, Mock
from apiclient.errors import HttpError

from ..googleplus import GooglePlusAPI
from ..conf import DEFAULT_PLUGIN_TEMPLATES
from ..globals import RECENT, ITALIAN

TEST_DEVELOPER_KEY = '123'
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

__all__ = [
    'GooglePlusAPITestCase',
    'GooglePlusPluginTestCase',
    'GooglePlusAPITestCaseWithErrors'
]



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
        activity_list = self.google_plus_api.get_search_activity_list(query='test', order_by=RECENT,
                                                                      preferred_language=ITALIAN)
        self.assertEqual(len(activity_list), 20)
        self.assertEqual(activity_list[0]['actor']['displayName'], 'Google')


class GooglePlusAPITestCaseWithErrors(TestCase):

    error_content = '{\n "error": {\n  "errors": [\n   {\n    "domain": "usageLimits",\n' \
                    '"reason": "keyInvalid",\n    "message": "Bad Request"\n   }\n  ],\n' \
                    '"code": 400,\n  "message": "Bad Request"\n }\n}\n'
    error_resp_dict = {'status': '400', 'x-xss-protection': '1; mode=block', 'x-content-type-options': 'nosniff',
                       'transfer-encoding': 'chunked', 'expires': 'Sun, 18 Aug 2013 07:25:24 GMT', 'server': 'GSE',
                       'cache-control': 'private, max-age=0', 'date': 'Sun, 18 Aug 2013 07:25:24 GMT',
                       'x-frame-options': 'SAMEORIGIN', 'content-type': 'application/json; charset=UTF-8'}

    def test_api_returns_unexpected_values(self):
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.return_value": 'whoops',
            "activities.return_value.search.return_value.execute.return_value": 'whoops'
        })
        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            user_activity_list = google_plus_api.get_user_activity_list(user_id='test')
            self.assertEqual(user_activity_list, [])
            search_activity_list = google_plus_api.get_search_activity_list(query='test')
            self.assertEqual(search_activity_list, [])

    def test_api_fails_silenty_if_http_error_on_production(self):
        mock = Mock()

        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.side_effect": HttpError(
                content=self.error_content,resp=Response(self.error_resp_dict)),
            "activities.return_value.search.return_value.execute.side_effect": HttpError(
                content=self.error_content, resp=Response(self.error_resp_dict))
        })
        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            user_activity_list = google_plus_api.get_user_activity_list(user_id='test')
            self.assertEqual(user_activity_list, [])
            search_activity_list = google_plus_api.get_search_activity_list(query='test')
            self.assertEqual(search_activity_list, [])

    @override_settings(DEBUG=True)
    def test_api_fails_loudly_on_development(self):
        mock = Mock()

        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.side_effect": HttpError(
                content=self.error_content,resp=Response(self.error_resp_dict)),
            "activities.return_value.search.return_value.execute.side_effect": HttpError(
                content=self.error_content, resp=Response(self.error_resp_dict))
        })
        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            self.assertRaises(HttpError, google_plus_api.get_user_activity_list, {'user_id': 'test'})
            self.assertRaises(HttpError, google_plus_api.get_search_activity_list, {'query': 'test'})


class GooglePlusPluginTestCase(BaseGooglePlusTestCase):

    def setUp(self):
        super(GooglePlusPluginTestCase, self).setUp()
        self.page = create_page("render test", "nav_playground.html", "en")
        self.ph = self.page.placeholders.get(slot="body")

    def test_plugin_user_activity_list(self):
        self.assertEqual(CMSPlugin.objects.all().count(), 0)
        google_plus_plugin = add_plugin(self.ph, "GooglePlusActivitiesPlugin", "en", google_user="test",
                                        render_template=DEFAULT_PLUGIN_TEMPLATES[0][0])
        self.page.publish()
        self.assertEqual(CMSPlugin.objects.filter(placeholder__page__publisher_is_draft=False).count(), 1)
        response = self.client.get(self.page.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['activity_list']), 20)

    def test_plugin_search_activity_list(self):
        self.assertEqual(CMSPlugin.objects.all().count(), 0)
        google_plus_plugin = add_plugin(self.ph, "GooglePlusActivitiesPlugin", "en", query="test",
                                        render_template=DEFAULT_PLUGIN_TEMPLATES[0][0])
        self.page.publish()
        self.assertEqual(CMSPlugin.objects.filter(placeholder__page__publisher_is_draft=False).count(), 1)
        response = self.client.get(self.page.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['activity_list']), 20)




