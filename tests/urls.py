from django.urls import path
from tests import views

urlpatterns = [
    path('tests/<str:function_name>', views.run_test, name='run_test'),
]