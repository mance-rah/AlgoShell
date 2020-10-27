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

class SentenceReverse(unittest.TestCase):
    def test_case_1(self):
        input = [" "," "]

        expected = [" "," "]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_2(self):

        input = ["a"," "," ","b"]

        expected = ["b"," "," ","a"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        input = ["h","e","l","l","o"]

        expected = ["h","e","l","l","o"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        input = ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]

        expected = ["p","r","a","c","t","i","c","e"," ","m","a","k","e","s"," ","p","e","r","f","e","c","t"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        input = ["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]

        expected = ["m","a","y"," ","t","h","e"," ","f","o","r","c","e"," ","b","e"," ","w","i","t","h"," ","y","o","u"]
        actual = sentence_reverse(input)
      
        self.assertEqual(expected, actual)

    def test_case_6(self):
        input = ["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]

        expected = ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

class PancakeSort(unittest.TestCase):
    def test_case_1(self):
        arr = [1]

        expected = [1]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        arr = [1,2]

        expected = [1,2]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_3(self):
        arr = [1,3,1]

        expected = [1,1,3]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        arr = [3,1,2,4,6,5]

        expected = [1,2,3,4,5,6]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        arr = [10,9,8,7,6,5,4,3,2,1]

        expected = [1,2,3,4,5,6,7,8,9,10]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        arr = [10,9,8,6,7,5,4,3,2,1,9,10,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1]

        expected = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

class ArrayOfArrayProducts(unittest.TestCase):
    def test_case_1(self):
        input = []
        expected = []

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        input = [1]
        expected = []

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)    

    def test_case_3(self):
        input = [2,2]
        expected = [2,2]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)
    
    def test_case_4(self):
        input = [2,7,3,4]
        expected = [84,24,56,42]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)    

    def test_case_5(self):
        input = [2,3,0,982,10]
        expected = [0,0,58920,0,0]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)
    
    def test_case_6(self):
        input = [-3,17,430,-6,5,-12,-11,5]
        expected = [-144738000,25542000,1009800,-72369000,86842800,-36184500,-39474000,86842800]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)

class SalesPath(unittest.TestCase):
    class Node:
        def __init__(self, cost):
            self.cost = cost
            self.children = []
            self.parent = None
    
    def test_case_1(self):
        root = SalesPath.Node(0)    # Parent
        node_a = SalesPath.Node(5)
        node_b = SalesPath.Node(3)
        node_c = SalesPath.Node(6)
        node_d = SalesPath.Node(4)
        node_e = SalesPath.Node(2)
        node_f = SalesPath.Node(0)
        node_g = SalesPath.Node(1)
        node_h = SalesPath.Node(5)
        node_i = SalesPath.Node(1)
        node_j = SalesPath.Node(10)
        node_k = SalesPath.Node(1)

        root.children.append(node_a)
        root.children.append(node_b)
        root.children.append(node_c)

        node_a.parent = root
        node_a.children.append(node_d)

        node_b.parent = root
        node_b.children.append(node_e)
        node_b.children.append(node_f)

        node_c.parent = root
        node_c.children.append(node_g)
        node_c.children.append(node_h)

        node_d.parent = node_a

        node_e.parent = node_b
        node_e.children.append(node_i)

        node_f.parent = node_b
        node_f.children.append(node_j)

        node_g.parent = node_c

        node_h.parent = node_c

        node_i.parent = node_e
        node_i.children.append(node_k)

        node_j.parent = node_f

        node_k.parent = node_i

        expected = 7
        actual = get_cheapest_cost(root)

        self.assertEqual(expected, actual)

class AbsoluteValueSort(unittest.TestCase):
    def test_case_1(self):
        arr = [2,-7,-2,-2,0]

        expected = [0,-2,-2,2,-7]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        arr = [-2,1]

        expected = [1,-2]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_3(self):
        arr = [0,1,2]

        expected = [0,1,2]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        arr = [2,-1,-1,-1]

        expected = [-1,-1,-1,2]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        arr = [-2,3,5,-1,4]

        expected = [-1,-2,3,4,5]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        arr = [4,-1,6,-4,2,-1]

        expected = [-1,-1,2,-4,4,6]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_7(self):
        arr = [6,4,-5,0,-1,7,0]

        expected = [0,0,-1,4,-5,6,7]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_8(self):
        arr = [-7,-2,-2,6,5,-6,-2,-6]

        expected = [-2,-2,-2,5,-6,-6,6,-7]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_9(self):
        arr = [-4,9,-1,1,-1,2,-8,-6,3]

        expected = [-1,-1,1,2,3,-4,-6,-8,9]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

