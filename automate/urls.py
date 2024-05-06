from django.urls import path
from django.http import HttpResponse
from automate.views import home

urlpatterns = [
    path('', home), # HOME
]
