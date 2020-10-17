# ======================================================
# Required setup to access models before starting server
# ======================================================
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

# ======================================================
# Questions config
# ======================================================

question_info_list = [
    {
        'name': 'Is Palindrome',
        'description': 'Write a function that takes in a string and returns True if it is a palindrome and False otherwise.\n\nA palindrome is a string that is read the same way forward as backwards.',
        'category': 'Strings', 
        'difficulty': 'Easy',
        'function_name': 'is_palindrome',
        'parameters': ['string'],
        'test_cases': [
            {'input': ['abcdcba'], 'output': True},
            {'input': ['a'], 'output': True},
            {'input': ['ab'], 'output': False}
        ]
    },
    {
        'name': 'Two Number Sum',
        'description': 'Given an array of integers and a target integer, return the two numbers in the list such that they add up to target.',
        'category': 'Arrays',
        'difficulty': 'Easy',
        'function_name': 'two_number_sum',
        'parameters': ['array', 'target_sum']
        'test_cases': [
            {'input': [[3, 5, -4, 8, 11, 1, -1, 6], 10], 'output': [-1, 11]}
        ]
    }
]

# ======================================================
# Sync questions config with the database
# ======================================================

from questions.models import Question, Category, Difficulty

for question_info in question_info_list:
    # Create category if it does not already exist
    if Category.objects.filter(name=question_info['category']).count() == 0:
        category = Category.objects.create(name=question_info['category'])
    else:
        category = Category.objects.get(name=question_info['category'])
    
    # Create difficulty if it does not already exist
    if Difficulty.objects.filter(name=question_info['difficulty']).count() == 0:
        difficulty = Difficulty.objects.create(name=question_info['difficulty'])
    else:
        difficulty = Difficulty.objects.get(name=question_info['difficulty'])

    # Create current question from config
    new_question = Question.objects.create(
        name=question_info['name'],
        description=question_info['description'],
        category=category,
        difficulty=difficulty,
        function_name=question_info['function_name'],
        parameters=question_info['parameters'],
        test_cases=question_info['test_cases']
    )