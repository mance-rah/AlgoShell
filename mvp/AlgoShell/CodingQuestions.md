# Coding Questions

## Is Palindrome
Write a function that takes in a string and
returns True if the string is a palindrome
otherwise False.

A palindrome is a string that is written the same
way forward as backwards. Note that single-character
strings are palindromes.

### Examples

```python
# Input
string = 'abcdcba'

# Output
True
```

### Directions
1. Write your solution in `solutions/is_palindrome.py`
2. Test your solution with `./AlgoShell.sh IsPalindrome`

## Plan Meeting

Implement a function `meeting_planner` that given the availability, `slots_a` and `slots_b`, of two people and a meeting duration `dur`, returns the earliest time slot that works for both of them and is of duration `dur`. If there is no common time slot that satisfies the duration requirement, return an empty array.

Time is given in a format called epoch, which is a nonnegative integer holding the number of minutes that have elapsed since an arbitrary point in time.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable `dur` is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

### Examples
```python
# Input
slots_a = [[10, 50], [60, 120], [140, 210]]
slots_b = [[0, 15], [60, 70]]
dur = 8

# Output
[60, 68]
```

```python
# Input
slots_a = [[10, 50], [60, 120], [140, 210]]
slots_b = [[0, 15], [60, 70]]
dur = 12

# Output
[]
```

### Directions
1. Write your solution in `solutions/plan_meeting.py`
2. Test your solution with `./AlgoShell.sh PlanMeeting`


