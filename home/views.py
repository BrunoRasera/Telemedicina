from django.shortcuts import render
from .models import Medicos

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request, 'sobre.html')

#chama os médicos do banco para retornar na página
def medico(request):
    medico = Medicos.objects.all()
    return render(request, 'medicos.html')