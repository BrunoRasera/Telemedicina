from django.urls import path 
from . import views

urlpatterns = [
    path('feedback_plataforma', views.feedback_plataforma, name='feedback_plataforma'),
]