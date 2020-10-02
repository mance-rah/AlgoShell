from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class IsPalindromeTests(APITestCase):

    def test_correct_solution_passes(self):
        """
        Ensure correct solution passes test cases.
        """
        request_body = {
            'solution': 'def is_palindrome(string):\n    for i in range(len(string)):\n        if string[i] != string[len(string) - 1 - i]:\n            return False\n    return True'
        }
        url = reverse('run_test', kwargs={'function_name': 'is_palindrome'})
        expected_response_body = {
            'passed': True,
            'results': [
                {
                    'inputs': {'string': 'abcdcba'},
                    'expected': True,
                    'actual': True
                },
                {
                    'inputs': {'string': 'a'},
                    'expected': True,
                    'actual': True
                },
                {
                    'inputs': {'string': 'ab'},
                    'expected': False,
                    'actual': False
                }
            ]
        }

        response = self.client.post(url, request_body, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)

    def test_false_function_fails(self):
        """
        Ensure function that always returns False failes test cases.
        """
        request_body = {
            'solution': 'def is_palindrome(string):\n    return False'
        }
        url = reverse('run_test', kwargs={'function_name': 'is_palindrome'})
        expected_response_body = {
            'passed': False,
            'results': [
                {
                    'inputs': {'string': 'abcdcba'},
                    'expected': True,
                    'actual': False
                },
                {
                    'inputs': {'string': 'a'},
                    'expected': True,
                    'actual': False
                },
                {
                    'inputs': {'string': 'ab'},
                    'expected': False,
                    'actual': False
                }
            ]
        }

        response = self.client.post(url, request_body, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)

    def test_true_function_fails(self):
        """
        Ensure function that always returns True failes test cases.
        """
        request_body = {
            'solution': 'def is_palindrome(string):\n    return True'
        }
        url = reverse('run_test', kwargs={'function_name': 'is_palindrome'})
        expected_response_body = {
            'passed': False,
            'results': [
                {
                    'inputs': {'string': 'abcdcba'},
                    'expected': True,
                    'actual': True
                },
                {
                    'inputs': {'string': 'a'},
                    'expected': True,
                    'actual': True
                },
                {
                    'inputs': {'string': 'ab'},
                    'expected': False,
                    'actual': True
                }
            ]
        }

        response = self.client.post(url, request_body, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)


        

