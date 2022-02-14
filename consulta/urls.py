from django.urls import path 
from . import views

urlpatterns = [
    path('agendaconsulta', views.agendaconsulta, name='agendaconsulta'),
    path('pagamentoconsulta', views.pagamentoconsulta, name='pagamentoconsulta'),
    path('visualizaconsulta', views.visualizaconsulta, name='visualizaconsulta')
]
