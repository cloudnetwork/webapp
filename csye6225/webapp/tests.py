from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
import sqlalchemy

class HealthzViewTests(TestCase):
    def test_healthz_returns_200(self):
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response.status_code, 200)

    def test_healthz_cache_control_header(self):
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response['Cache-Control'], 'no-cache, no-store, must-revalidate')

    @patch('webapp.views.sqlalchemy.create_engine')
    def test_healthz_with_database_connection(self, mock_create_engine):
        # Mock the create_engine method to return a mock connection object
        mock_connection = mock_create_engine.return_value.connect.return_value
        mock_create_engine.return_value.connect.return_value.__enter__.return_value = mock_connection

        # Check if the endpoint returns 200 when the database connection is valid
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response.status_code, 200)
