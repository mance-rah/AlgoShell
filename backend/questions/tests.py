from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Question, Category, Difficulty
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
                    'actual': True,
                    'passed': True
                },
                {
                    'inputs': {'string': 'a'},
                    'expected': True,
                    'actual': True,
                    'passed': True
                },
                {
                    'inputs': {'string': 'ab'},
                    'expected': False,
                    'actual': False,
                    'passed': True
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
                    'actual': False,
                    'passed': False
                },
                {
                    'inputs': {'string': 'a'},
                    'expected': True,
                    'actual': False,
                    'passed': False
                },
                {
                    'inputs': {'string': 'ab'},
                    'expected': False,
                    'actual': False,
                    'passed': True
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
                    'actual': True,
                    'passed': True
                },
                {
                    'inputs': {'string': 'a'},
                    'expected': True,
                    'actual': True,
                    'passed': True
                },
                {
                    'inputs': {'string': 'ab'},
                    'expected': False,
                    'actual': True,
                    'passed': False
                }
            ]
        }

        response = self.client.post(url, request_body, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)

class GetQuestionsTests(APITestCase):
    
    def setUp(self):
        create_test_questions()

    def test_is_palindrome_exists(self):
        """
        Ensure Is Palindrome endpoint question is returned
        """
        url = reverse('get_questions')
        expected_response_body = [
            {
                'title': 'Is Palindrome',
                'description': 'Write a function that determines if a string is a palindrome.',
                'function_name': 'is_palindrome',
                'function_signature': 'is_palindrome(string)',
                'category': 'Strings',
                'difficulty': 'Easy',
                'tests': [
                    {'inputs': {"string": "abcdcba"}, 'output': True},
                    {'inputs': {"string": "a"}, 'output': True},
                    {'inputs': {"string": "ab"}, 'output': False}
                ]
            }
        ]

        response = self.client.get(url, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)

from .helpers import save_suites

class TestSyncDatabaseWithSuitesConfig(TestCase):

    def setUp(self):
        create_test_questions()

    def test_helper_function(self):
        """
        Tests the ability of the test_suites helper function to save tests in correct Question
        """

        suites = [
            {"inputs": {"string": "abcdcba"}, "output": True},
            {"inputs": {"string": "a"}, "output": True},
            {"inputs": {"string": "ab"}, "output": True}
        ]

        save_suites(suites)

        is_palindrome_question = Question.objects.get(name='Is Palindrome')
        
        self.assertEqual(is_palindrome_question.tests, suites)

def create_test_questions():
    easy_difficulty = Difficulty.objects.create(name="Easy")
    strings_category = Category.objects.create(name="Strings")
    is_palindrome_question = Question.objects.create(
        name='Is Palindrome',
        signature='is_palindrome(string)',
        description='Write a function that determines if a string is a palindrome.',
        category=strings_category,
        difficulty=easy_difficulty,
    )



        

