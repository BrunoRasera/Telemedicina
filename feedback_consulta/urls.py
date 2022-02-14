from django.urls import path 
from . import views

urlpatterns = [
    path('feedback_consulta', views.feedback_consulta, name='feedback_consulta'),
]