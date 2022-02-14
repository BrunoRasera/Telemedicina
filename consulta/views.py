# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from consulta.models import Consulta
from .models import Medicos, Paciente, Medicos, Pagamento
from .forms import ConsultaForm


def pagamentoconsulta(request):
    if request.POST:
        return render(request, 'usuario/dashboard.html')
    return render(request, 'consulta/pagamentoconsulta.html')

def visualizaconsulta(request):
    user = request.user.username
    paciente = Paciente.objects.values_list('nome_paciente', flat=True)
    if user in paciente:
        idPaciente = Paciente.objects.filter(nome_paciente=user).values_list('id', flat=True)[0]
        consultas = Consulta.objects.values_list('paciente', flat=True)
        #print(consultas, idPaciente)
        if idPaciente in consultas:
            pac = Consulta.objects.filter(paciente=idPaciente).values_list()
            medico = Medicos.objects.values_list('nome_medico', flat=True)
            valor = Pagamento.objects.values_list('valor', flat=True)

            print(pac)
            return render(request, 'consulta/visualizaconsulta.html',{'pac': pac, 'valor': valor, 'medico':medico})
    return render(request, 'consulta/visualizaconsulta.html')

def agendaconsulta(request):
    if request.method == 'POST':
        data = request.POST['data']
        print(data)
        user = get_object_or_404(Paciente, pk=request.user.id)
        medico = Medicos.objects.get(id=1)
        pagamento = Pagamento.objects.get(id=1)
        print(user)
        consulta = Consulta.objects.create(paciente=user, data=data, medico=medico, pagamento=pagamento)
        consulta.save()
        return render(request, 'consulta/pagamentoconsulta.html')
    else:
        medicos = Medicos.objects.all()
        return render(request, 'consulta/agendaconsulta.html', {'medicos': medicos})
