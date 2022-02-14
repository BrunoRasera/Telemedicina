from django.urls import path 
from . import views

urlpatterns = [
    path('paciente', views.paciente, name='paciente'),
]