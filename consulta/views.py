# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from consulta.models import Consulta, Paciente
from .models import Medicos
from .forms import ConsultaForm


def pagamentoconsulta(request):
    return render(request, 'consulta/pagamentoconsulta.html')

def visualizaconsulta(request):
    pac = Consulta.objects.all()
    return render(request, 'consulta/visualizaconsulta.html',{'pac': pac})

def agendaconsulta(request):
    if request.method == 'POST':
        data = request.POST['data']
        print(data)
        user = get_object_or_404(Paciente, pk=request.user.id)
        print(user)
        consulta = Consulta.objects.create(paciente=user, data=data)
        consulta.save()
        return render(request, 'consulta/pagamentoconsulta.html')
    else:
        medicos = Medicos.objects.all()
        return render(request, 'consulta/agendaconsulta.html', {'medicos': medicos})
