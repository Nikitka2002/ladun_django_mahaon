from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viola_jones/', views.indexvj, name='index')
]
