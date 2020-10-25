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




