from django.urls import path 
from . import views

urlpatterns = [
    path('paciente_verconsulta', views.paciente_verconsulta, name='paciente_verconsulta')
]