from pyramid import testing

import unittest
import mock
import json
import test.fixtures as factory
from test.mock_helpers import MockQuery
from src.views import reference_triage, reference_triage_id, reference_triage_id_delete, reference_triage_id_update, reference_triage_promote


class ReferenceTriage(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    @mock.patch('src.models.DBSession.query')
    def test_should_return_valid_reference_triage(self, mock_search):
        rtriage = factory.ReferenceTriageFactory()
        mock_search.return_value = MockQuery(rtriage)

        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        #request.matchdict['id'] = rtriage.format_name
        response = reference_triage(request)

        self.assertEqual(response[0], rtriage.to_dict())

    @mock.patch('src.models.DBSession.query')
    def test_should_return_non_existent_reference_triage(self, mock_search):
        mock_search.return_value = MockQuery(None)

        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        #request.matchdict['id'] = 'nonexistent_id'
        response = reference_triage(request)
        self.assertEqual(response.status_code, 404)