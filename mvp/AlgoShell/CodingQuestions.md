# Coding Questions

### 1. Is Palindrome
Write a function that takes in a string and
returns True if the string is a palindrome
otherwise False.

A palindrome is a string that is written the same
way forward as backwards. Note that single-character
strings are palindromes.

**Sample Input:**
```python
string = 'abcdcba'
```
**Sample Output:**
```python
True
```
**Please follow these steps:**
1. Write your solution in `solutions/is_palindrome.py`
2. Test your solution with `./AlgoShell.sh IsPalindrome`

---

### 2. Sentence Reverse
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

**Sample Input:**
```python
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
           'm', 'a', 'k', 'e', 's', '  ',
           'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
```
**Sample Output:**
```python
[ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
  'm', 'a', 'k', 'e', 's', '  ',
  'p', 'e', 'r', 'f', 'e', 'c', 't' ]
```
**Please follow these steps:**
1. Write your solution in `solutions/sentence_reverse.py`
2. Test your solution with `./AlgoShell.sh SentenceReverse`

---

### 2. Bracket Match
A string of brackets is considered correctly matched if 
every opening bracket in the string can be paired up with 
a later closing bracket, and vice versa. For instance, “(())()” 
is correctly matched, whereas “)(“ and “((” aren’t. For 
instance, “((” could become correctly matched by adding 
two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function 
bracket_match that takes a bracket string as an input and 
returns the minimum number of brackets you’d need to 
add to the input in order to make it correctly matched.

**Sample Input:**
```python
text = '(()'
```
**Sample Output:**
```python
1
```
**Sample Input:**
```python
text = '(())'
```
**Sample Output:**
```python
0
```
**Sample Input:**
```python
text = '())('
```
**Sample Output:**
```python
2
```
**Please follow these steps:**
1. Write your solution in `solutions/bracket_match.py`
2. Test your solution with `./AlgoShell.sh BracketMatch`

---

### 3. Sentence Reverse
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

**Sample Input:**
```python
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
           'm', 'a', 'k', 'e', 's', '  ',
           'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
```
**Sample Output:**
```python
[ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
  'm', 'a', 'k', 'e', 's', '  ',
  'p', 'e', 'r', 'f', 'e', 'c', 't' ]
```
**Please follow these steps:**
1. Write your solution in `solutions/sentence_reverse.py`
2. Test your solution with `./AlgoShell.sh SentenceReverse`

---

### 4. Pancake Sort
1\) Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.

2\) Write a function pancake_sort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.

**Sample Input:**
```python
arr = [1, 5, 4, 3, 2]
```
**Sample Output:**
```python
[1, 2, 3, 4, 5]
```
**Please follow these steps:**
1. Write your solution in `solutions/pancake_sort.py`
2. Test your solution with `./AlgoShell.sh PancakeSort`

---

### 5. Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division.

**Sample Input:**
```python
input: arr = [8, 10, 2]
```
**Sample Output:**
```python
output: [20, 16, 80] # by calculating: [102, 82, 8*10]
```

**Sample Input:**
```python
input: arr = [2, 7, 3, 4]
```
**Sample Output:**
```python
output: [84, 24, 56, 42] # by calculating: [734, 234, 274, 273]
```

**Please follow these steps:**
1. Write your solution in `solutions/array_of_array_products.py`
2. Test your solution with `./AlgoShell.sh ArrayOfArrayProducts`