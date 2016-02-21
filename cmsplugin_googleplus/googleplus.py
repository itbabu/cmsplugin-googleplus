from __future__ import unicode_literals

import logging

from django.utils.translation import ugettext_lazy as _
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

logger = logging.getLogger(__name__)


class GooglePlusAPI(object):
    """
    Simple wrapper for the Google Plus API.
    The Google documentation is
    `here <https://developers.google.com/+/api/latest/>`_.
    """
    def __init__(self, developer_key):
        """
        Builds a Google Plus service object.

        :param developer_key: Key for controlling API usage, obtained from the
            `API Console <https://code.google.com/apis/console>`_.
        :type developer_key: str
        """
        self.service = build(
            serviceName='plus', version='v1', developerKey=developer_key)

    def get_user_activity_list(self, user_id, collection='public', results=10):
        """
        Get a list is activities from a Google Plus User. An activity is a note
         that a user posts to their stream.
        The Google documentation is
        `here <https://developers.google.com/+/api/latest/activities>`_.

        :param collection: The collection of activities to list
        :param user_id: The ID of the user to get activities for
        :param results: The number of activities to include in the response
            for any response, the actual number returned might be less than the
            specified results.
            To keep the application simple acceptable values are 1 to 20,
            inclusive. Default is 10.
        :type collection: str
        :type user_id: unicode or str
        :type results: unsigned integer
        :raises: TypeError, ValueError
        :returns: The list of user activities and an alert message, if any.
        """
        if self.service:
            try:
                activities_resource = self.service.activities()
                request = activities_resource.list(
                    userId=user_id, collection=collection,
                    maxResults=results, fields='items')
                activities_document = request.execute()
                if 'items' in activities_document:
                    return activities_document['items'], ''
                else:
                    return [], _('No items found')
            except HttpError as e:
                error_msg = _('Google Plus API error: `%s`' % (e, ))
                logger.error(error_msg)
                return [], error_msg

    def get_search_activity_list(self, query, preferred_language=None,
                                 order_by=None, results=10):
        """
        Get a list is activities from a Google Plus User. An activity is a note
         that a user posts to their stream.
        The Google documentation is
        `here <https://developers.google.com/+/api/latest/activities>`_.

        :param query: Full-text search query string.
        :param preferred_language: Specify the preferred language to search
            with.
            See `search language codes
            <https://developers.google.com/+/api/#pagination>`_ for available
            values.
        :param order_by: Specifies how to order search results.
            Acceptable values are:
            "best": Sort activities by relevance to the user, most relevant
                first.
            "recent": Sort activities by published date, most recent first.
                (default)
        :param results: The number of activities to include in the response
            for any response, the actual number returned might be less than the
             specified results.
            To keep the application simple acceptable values are 1 to 20,
            inclusive. Default is 10.

        :type query: unicode
        :type preferred_language: str
        :type order_by: str
        :type results: unsigned integer

        :returns: The list of activities, result of the search an alert message, if any.
        """
        if self.service:
            try:
                activities_resource = self.service.activities()
                data = {
                    'query': query, 'maxResults': results, 'fields': 'items'}
                if preferred_language:
                    data.update({'language': preferred_language})
                if order_by:
                    data.update({'orderBy': order_by})
                request = activities_resource.search(**data)
                activities_document = request.execute()
                if 'items' in activities_document:
                    return activities_document['items'], ''
                else:
                    return [], _('No items found')
            except HttpError as e:
                error_msg = _('Google Plus API error: `%s`' % (e,))
                logger.error(error_msg)
                return [], error_msg
