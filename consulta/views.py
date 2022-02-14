# Create your views here.
from django.shortcuts import render,redirect

from consulta.models import Consulta
from .models import Consulta
from .forms import ConsultaForm


def paciente_verconsulta(request):
    # Get all
    pac = Consulta.objects.all()
    #med = Medicos.objects.get()
    print("Myoutput",pac)
    return render(request,'paciente_verconsulta.html',{'pac': pac})
    
def pagamentoconsulta(request):
    return render(request, 'consulta/pagamentoconsulta.html')

def visualizaconsulta(request):
    return render(request, 'consulta/visualizaconsulta.html')

def agendaconsulta(request):
    return render(request, 'consulta/agendaconsulta.html')
