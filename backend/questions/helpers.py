import json
from .models import Question

SUITES_JSON_FILENAME = 'questions/suites.json'

def save_suites(suites):
    """
    Saves suites in corresponding Question

    Parameters:
        - suites (dict): Function names as keys and test list as values
    """
    questions_list = Question.objects.all()

    for question in questions_list:
        question.tests = suites
        question.save()

def get_suite(function_name):
    """
    Reads suites dictionary from adjacent JSON file.

    Parameters:
        - function_name (str): Name of function being tested

    Returns: 
        - list: JSON objects with inputs and output as keys
    """

    suites_dict = read_suites()
    return suite_dict[function_name]

def read_suites():
    """
    Reads adjacent JSON file.

    Returns: 
        - dict: JSON data
    """

    with open(SUITES_JSON_FILENAME) as file:
        suites_dict = json.load(file)
    return suites_dict