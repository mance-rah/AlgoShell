import unittest
from suites import get_suite

class TestReadSuitesList(unittest.TestCase):
    
    def test_is_palindrome(self):
        expected_suites_list = [
            {"inputs": {"string": "abcdcba"}, "output": True},
            {"inputs": {"string": "a"}, "output": True},
            {"inputs": {"string": "ab"}, "output": False}
        ]

        actual_suites_list = get_suite('is_palindrome')

        self.assertEqual(expected_suites_list, actual_suites_list)

