import unittest
from add_two_numbers import add_two_numbers
import time

class TestAddTwoNumbers(unittest.TestCase):

    def test_1_1(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_2_2(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_3_3(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_4_4(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_5_5(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_6_6(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_7_7(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_8_8(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_9_9(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_10_10(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_11_11(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_12_12(self):
        a, b = 2, 2
        expected = 4

        actual = add_two_numbers(a, b)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    for i in range(1, 13):
        time.sleep(0.25)
        print('Running test case {}'.format(i))
    unittest.main()