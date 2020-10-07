from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .helpers import get_suite
import json
    
@api_view(['POST'])
@parser_classes([JSONParser])
def run_test(request, function_name):
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
                'passed': locals()['result'] == case['output']
            }
        )

    return JsonResponse(response_body)
