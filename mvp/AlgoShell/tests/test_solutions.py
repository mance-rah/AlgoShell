import unittest
from solutions import *

class IsPalindrome(unittest.TestCase):
    def test_case_1(self):
        string = 'abcdcba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        string = 'a'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        string = 'ab'

        expected = False
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        string = 'aba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        string = 'abb'

        expected = False
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        string = 'abba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_7(self):
        string = 'abcdefghhgfedcba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_8(self):
        string = 'abcdefghihgfedcba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_9(self):
        string = 'abcdefghihgfeddcba'

        expected = False
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

class BracketMatch(unittest.TestCase):
    def test_case_1(self):
        text = ')'

        expected = 1
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        text = '('

        expected = 1
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        text = '(())'

        expected = 0
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        text = '(()'

        expected = 1
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        text = '())('

        expected = 2
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        text = '))))'

        expected = 4
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_7(self):
        text = ')('

        expected = 2
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_8(self):
        text = '()()()()()'

        expected = 0
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()