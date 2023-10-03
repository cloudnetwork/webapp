from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HealthzViewTests(TestCase):
    def test_healthz_no_payload(self):
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response.status_code, 200)

    def test_healthz_cache_control_header(self):
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response['Cache-Control'], 'no-cache, no-store, must-revalidate')

    def test_healthz_database_connection(self):
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response.status_code, 200)

        with self.settings(DATABASES={'default': {}}):
            response = self.client.get(reverse('healthz'))
        self.assertEqual(response.status_code, 503)
