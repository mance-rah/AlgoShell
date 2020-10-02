from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class RunTestTests(APITestCase):
    def test_hello_world(self):
        """
        Ensure hello world message is returned.
        """
        request_body = {'solution': 'Insert solution here'} 
        url = reverse('run_test', kwargs={'function_name':'Insert function name here'})
        expected_response_body = {'function_name': 'Insert function name here', 'solution': 'Insert solution here'}

        response = self.client.post(url, request_body, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)
        

