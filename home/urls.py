from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('areamedico', views.areamedico, name='areamedico'),
    path('areapaciente', views.areapaciente, name='areapaciente'),
    path('consulta', views.consulta, name='consulta')
]