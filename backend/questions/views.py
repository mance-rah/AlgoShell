from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import Question
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

@api_view(['GET'])
@parser_classes([JSONParser])
def get_questions(request):
    response_body = []

    for question in Question.objects.all():
        function_name = convert_title_to_function_name(question.name)
        test_suite = get_suite(function_name)

        response_body.append({
            'title': question.name,
            'description': question.description,
            'function_name': function_name,
            'function_signature': question.signature,
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
    
