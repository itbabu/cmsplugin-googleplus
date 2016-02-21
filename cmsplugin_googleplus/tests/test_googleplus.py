from __future__ import unicode_literals

from django.test import TestCase
from django.utils.encoding import force_text
from googleapiclient.errors import HttpError
from httplib2 import Response
from mock import Mock, patch

from ..globals import ITALIAN, RECENT
from ..googleplus import GooglePlusAPI
from .base import TEST_DEVELOPER_KEY, BaseGooglePlusTestCase

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
        activity_list, alert_message = self.google_plus_api.get_user_activity_list(
            user_id='test')
        self.assertEqual(len(activity_list), 20)
        self.assertEqual(activity_list[0]['actor']['displayName'], 'Google')

    def test_search_activity_list_fetching(self):
        activity_list, alert_message = self.google_plus_api.get_search_activity_list(
            query='test', order_by=RECENT,
            preferred_language=ITALIAN)
        self.assertEqual(len(activity_list), 20)
        self.assertEqual(activity_list[0]['actor']['displayName'], 'Google')


class GooglePlusAPITestCaseWithErrors(TestCase):
    error_content = b'{\n "error": {\n  "errors": [\n   {\n    "domain": ' \
                    b'"usageLimits",\n"reason": "keyInvalid",\n    ' \
                    b'"message": "Bad Request"\n   }\n  ],\n' \
                    b'"code": 400,\n  "message": "Bad Request"\n }\n}\n'
    error_resp_dict = {'status': '400', 'x-xss-protection': '1; mode=block',
                       'x-content-type-options': 'nosniff',
                       'transfer-encoding': 'chunked',
                       'expires': 'Sun, 18 Aug 2013 07:25:24 GMT',
                       'server': 'GSE',
                       'cache-control': 'private, max-age=0',
                       'date': 'Sun, 18 Aug 2013 07:25:24 GMT',
                       'x-frame-options': 'SAMEORIGIN',
                       'content-type': 'application/json; charset=UTF-8'}

    def test_get_search_activity_list_returns_unexpected_values(self):
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.search.return_value.execute.return_value": 'whoops'
        })

        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            search_activity_list, alert_message = google_plus_api.get_search_activity_list(
                query='test')
            self.assertEqual(search_activity_list, [])
            self.assertEqual(force_text(alert_message), 'No items found')

    def test_get_user_activity_list_returns_unexpected_values(self):
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.return_value": 'whoops',
        })

        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            user_activity_list, alert_message = google_plus_api.get_user_activity_list(
                user_id='test')
            self.assertEqual(user_activity_list, [])

            self.assertEqual(force_text(alert_message), 'No items found')

    def test_staff_gets_alert_if_http_error_on_user_activity_list(self):
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.side_effect":
                HttpError(
                    content=self.error_content,
                    resp=Response(self.error_resp_dict)),
        })

        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            user_activity_list, alert_one = google_plus_api.get_user_activity_list(
                user_id='test')
            self.assertEqual(user_activity_list, [])
            self.assertEqual(alert_one, 'Google Plus API error: `<HttpError 400 "Bad Request">`')

    def test_staff_gets_alert_if_http_error_on_search_activity_list(self):
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.search.return_value.execute.side_effect":
                HttpError(
                    content=self.error_content,
                    resp=Response(self.error_resp_dict))
        })

        with patch("cmsplugin_googleplus.googleplus.build", return_value=mock):
            google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)
            search_activity_list, alert = google_plus_api.get_search_activity_list(
                query='test')
            self.assertEqual(search_activity_list, [])
            self.assertEqual(alert, 'Google Plus API error: `<HttpError 400 "Bad Request">`')
