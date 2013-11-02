from __future__ import unicode_literals

from httplib2 import Response
from django.test.utils import override_settings
from django.test import TestCase
from mock import patch, Mock
from apiclient.errors import HttpError

from .base import TEST_DEVELOPER_KEY, BaseGooglePlusTestCase
from ..googleplus import GooglePlusAPI
from ..globals import RECENT, ITALIAN


__all__ = [
    'GooglePlusAPITestCase',
    'GooglePlusAPITestCaseWithErrors'
]


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
                content=self.error_content, resp=Response(self.error_resp_dict)),
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