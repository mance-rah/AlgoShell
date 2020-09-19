from rest_framework import viewsets
from TestRequestService.tests.serializers import QuestionSerializer

class TestRunner(viewsets.ModelViewSet):
    """
    API endpoint that runs solutions against test cases.
    """
    pass