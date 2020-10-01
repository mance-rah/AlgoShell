from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows uers to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
@csrf_exempt
def run_test(request, function_name):
    """
    Echos the information that was sent to the endpoints in the response.
    Will later be used for running tests contained in solution from request.

    Request body: {solution:str}
    Endpoint URL: tests/<question_name>
    Response Body: {question_name:str, solution:str}
    """
    return JsonResponse({"message": "Hello, World!"})

