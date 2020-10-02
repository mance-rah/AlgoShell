from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json
    
@api_view(['POST'])
@parser_classes([JSONParser])
def run_test(request, function_name):
    """
    Echos the information that was sent to the endpoints in the response.
    Will later be used for running tests contained in solution from request.

    Request body: {solution:str}
    Endpoint URL: tests/<question_name>
    Response Body: {question_name:str, solution:str}
    """
    suite = get_suite(function_name)

    # Get solution as a string from request
    solution = request.data['solution']

    # Define solution str as python function
    exec(solution)

    # Run test suite on function
    response_body = {'passed': True, 'results': []}

    for case in suite:
        exec('result = {}("{}")'.format(function_name, case['inputs']['string']))
        if locals()['result'] != case['output']:
            response_body['passed'] = False
        
        response_body['results'].append(
            {
                'inputs': case['inputs'],
                'expected': case['output'],
                'actual': locals()['result'],
            }
        )

    return JsonResponse(response_body)

# ================
# Helper functions
# ================


SUITES_JSON_FILENAME = 'tests/suites.json'

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
