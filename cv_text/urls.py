from django.urls import path, include
from django.views.generic import ListView, DetailView
from cv_text.models import Text
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Text.objects.all(), template_name="")),
]
