from django.urls import reverse_lazy
from django.test import TestCase

class TestRegistration(TestCase):

    def test_registration_page_status_code(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200, msg="Register page status code isn't 200")

    def test_registration_page_reverse_lazy_status_code(self):
        response_reverse_lazy = self.client.get(reverse_lazy('registration'))
        self.assertEqual(response_reverse_lazy.status_code, 200, msg="Register page reverse lazy status code isn't 200")

    def test_registration_page_template(self):
        response = self.client.get(reverse_lazy('registration'))
        self.assertTemplateUsed(response, 'users/register.html')
