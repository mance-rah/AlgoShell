from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import Question
import json
    
@api_view(['POST'])
@parser_classes([JSONParser])
def run_test(request, function_name):
    suite = Question.objects.get(function_name=function_name).test_cases

    # Get solution as a string from request
    solution = request.data['solution']

    # Define solution str as python function
    exec(solution)

    # Run test suite on function
    response_body = {'passed': True, 'results': []}

    for case in suite:
        get_result_code_str = 'result = {}({})'.format(function_name, _param_value_list_to_str(list(case['input'].values())))
        exec(get_result_code_str)

        if locals()['result'] != case['output']:
            response_body['passed'] = False
        
        response_body['results'].append(
            {
                'inputs': case['input'],
                'expected': case['output'],
                'actual': locals()['result'],
                'passed': locals()['result'] == case['output']
            }
        )

    return JsonResponse(response_body)

def _param_value_list_to_str(param_value_list):
    """Given a list of parameter values return a string with the values separated with commas and spaces in between them."""
    param_value_str = ''
    for value in param_value_list:
        if type(value) is str:
            param_value_str += '"{}", '.format(value)
        else:
            param_value_str += '{}, '.format(value)

    # Do not include the last comma and space in result
    return param_value_str[:-2]


@api_view(['GET'])
@parser_classes([JSONParser])
def get_questions(request):
    response_body = []

    for question in Question.objects.all():
        function_name = convert_title_to_function_name(question.name)
        test_suite = question.test_cases

        response_body.append({
            'title': question.name,
            'description': question.description,
            'function_name': question.function_name,
            'parameters': question.parameters,
            'category': question.category.name,
            'difficulty': question.difficulty.name,
            'tests': test_suite
        })

        return JsonResponse(response_body, safe=False)

def convert_title_to_function_name(title):
    function_name = ''
    for word in title.split(' '):
        function_name += word.lower() + '_'
    return function_name[:-1]    
    
