import json

SUITES_JSON_FILENAME = 'suites.json'

def get_suite(function_name):
    """
    Reads suites dictionary from adjacent JSON file.

    Parameters:
        - function_name (str): Name of function being tested

    Returns: List of JSON objects with inputs and output as keys
    """

    suites_dict = read_suites()
    return suites_dict[function_name]

def read_suites():
    """
    Reads adjacent JSON file.

    Returns: JSON data (dict)
    """

    with open(SUITES_JSON_FILENAME) as file:
        suites_dict = json.load(file)
    return suites_dict