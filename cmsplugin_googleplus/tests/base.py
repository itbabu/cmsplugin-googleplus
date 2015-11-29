from __future__ import unicode_literals

import json
import os

from django.test import TestCase
from mock import Mock, patch

from ..googleplus import GooglePlusAPI

TEST_DEVELOPER_KEY = '123'
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def data_from_file(filename):
    path = os.path.join(DATA_DIR, filename)
    f = open(path, 'r')
    data = f.read()
    f.close()
    return json.loads(data)


class BaseGooglePlusTestCase(TestCase):
    def setUp(self):
        super(BaseGooglePlusTestCase, self).setUp()
        # TODO: improve this. apiclient.http.HttpMock should be used as
        # argument in apiclient.http.HttpRequest.execute.
        mock = Mock()
        mock.configure_mock(**{
            "activities.return_value.list.return_value.execute.return_value":
                data_from_file('activities.json'),
            "activities.return_value.search.return_value.execute.return_value":
                data_from_file('activities.json')
        })
        self.patcher = patch(
            "cmsplugin_googleplus.googleplus.build", return_value=mock)
        self.patcher.start()
        self.google_plus_api = GooglePlusAPI(TEST_DEVELOPER_KEY)

    def tearDown(self):
        self.patcher.stop()
