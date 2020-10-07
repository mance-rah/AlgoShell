from django.urls import path
from questions import views

urlpatterns = [
    path('questions/<str:function_name>', views.run_test, name='run_test'),
]