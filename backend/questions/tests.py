from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Question, Category, Difficulty
import json

APITestCase.maxDiff = None

def create_is_palindrome_question():

    Question.objects.create(
        name='Is Palindrome',
        description='Write a function that determines if a string is a palindrome.',
        category=Category.objects.create(name="Strings"),
        difficulty=Difficulty.objects.create(name="Easy"),
        function_name='is_palindrome',
        parameters=['string'],
        test_cases = [
            {'input': ['abcdcba'], 'output': True},
            {'input': ['a'], 'output': True},
            {'input': ['ab'], 'output': False}
        ]
    )

class CreateSuiteTests(APITestCase):

    def setUp(self):
        create_is_palindrome_question()

    def test_cases_correct_definitions(self):
        """Ensure tests are formatted correctly when reading."""
        question = Question.objects.get(name='Is Palindrome')
        expected = [
            {'input': {'string': 'abcdcba'}, 'output': True},
            {'input': {'string': 'a'}, 'output': True},
            {'input': {'string': 'ab'}, 'output': False}
        ]
        actual = question.test_cases

        self.assertEqual(expected, actual)

class TwoNumberSumTests(APITestCase):
    
    def setUp(self):
        # Create two number sum question
        Question.objects.create(
            name='Two Number Sum',
            description='Mock description',
            category= Category.objects.create(name='Mock category'),
            difficulty=Difficulty.objects.create(name='Mock difficulty'),
            function_name='two_number_sum',
            parameters=['array', 'target_sum'],
            test_cases= [
                {'input': [[3, 5, -4, 8, 11, 1, -1, 6], 10], 'output': [-1, 11]}
            ]
        )

    def test_correct_solution_passes(self):
        """
        Ensure correct solution passes test cases.
        """
        solution = "" + \
        "def two_number_sum(array, targetSum):\n" + \
        "   comps = {targetSum - value: value for value in array}\n" + \
        "   for value in array:\n" + \
        "       if value in comps and comps[value] != value:\n" + \
        "           return [comps[value], value]\n" + \
        "   return []"

        request_body = {
            'solution': solution
        }
        url = reverse('run_test', kwargs={'function_name': 'two_number_sum'})
        expected_response_body = {
            'passed': True,
            'results': [
                {
                    'inputs': {
                        'array': [3, 5, -4, 8, 11, 1, -1, 6],
                        'target_sum': 10
                    },
                    'expected': [-1, 11],
                    'actual': [-1, 11],
                    'passed': True
                }
            ]
        }

        response = self.client.post(url, request_body, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)

class IsPalindromeTests(APITestCase):

    def setUp(self):
        create_is_palindrome_question()

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
        create_is_palindrome_question()

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
                'parameters': ['string'],
                'category': 'Strings',
                'difficulty': 'Easy',
                'tests': [
                    {'input': {"string": "abcdcba"}, 'output': True},
                    {'input': {"string": "a"}, 'output': True},
                    {'input': {"string": "ab"}, 'output': False}
                ]
            }
        ]

        response = self.client.get(url, format='json')
        actual_response_body = json.loads(response.content)

        self.assertEqual(expected_response_body, actual_response_body)



