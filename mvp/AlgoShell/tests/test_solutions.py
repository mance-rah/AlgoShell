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

class PlanMeeting(unittest.TestCase):
    
    def test_case_1(self):
        slots_a = [[7, 12]]
        slots_b = [[2, 11]]
        dur = 5

        expected = []
        actual = plan_meeting(slots_a, slots_b, dur)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        slots_a = [[6, 12]]
        slots_b = [[2, 11]]
        dur = 5

        expected = [6, 11]
        actual = plan_meeting(slots_a, slots_b, dur)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        slots_a = [[1, 10]]
        slots_b = [[2, 3], [5, 7]]
        dur = 2

        expected = [5, 7]
        actual = plan_meeting(slots_a, slots_b, dur)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        slots_a = [[0, 5], [50, 70], [120, 125]]
        slots_b = [[0, 50]]
        dur = 8

        expected = []
        actual = plan_meeting(slots_a, slots_b, dur)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        slots_a = [[10, 50], [60, 120], [140, 210]]
        slots_b = [[0, 15], [60, 70]]
        dur = 8

        expected = [60, 68]
        actual = plan_meeting(slots_a, slots_b, dur)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        slots_a = [[10, 50], [60, 120], [140, 210]]
        slots_b = [[0, 15], [60, 72]]
        dur = 12

        expected = [60, 72]
        actual = plan_meeting(slots_a, slots_b, dur)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()