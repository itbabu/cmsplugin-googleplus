from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import GooglePlusActivities

__all__ = [
    'GooglePlusActivitiesTestCase'
]


class GooglePlusActivitiesTestCase(TestCase):

    def test_user_or_search(self):
        """Test a validator: you must enter a query or a google+ user id."""
        google_plus_activities = GooglePlusActivities()
        self.assertRaises(ValidationError, google_plus_activities.clean)
        google_plus_activities.query = 'test'
        google_plus_activities.clean()
        google_plus_activities.query = None
        google_plus_activities.google_user = 'test_user'
        google_plus_activities.clean()

    def test_unicode(self):
        google_plus_activities = GooglePlusActivities(query='test')
        google_plus_activities.__unicode__()
        google_plus_activities.query = None
        google_plus_activities.google_user = 'test_user'
        google_plus_activities.__unicode__()