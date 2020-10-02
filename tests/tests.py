from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class RunTestTests(APITestCase):
    def test_hello_world(self):
        """
        Ensure hello world message is returned.
        """
        url = reverse('run_test', kwargs={'function_name':'is_palindrome'})
        expected_response = {'message': 'Hello, World!'}
        actual_response = self.client.get(url, format='json')
        self.assertEqual(expected_response, json.loads(actual_response.content))
        

