from django.urls import include, path
from django.contrib import admin

from rest_framework import routers
from tests import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tests.urls')),
]
