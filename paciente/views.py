from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from django.contrib.auth.models import User
from .forms import PacienteForm

def paciente(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        email = request.POST['email']
        nome_paciente = request.POST['nome_paciente']
        rg = request.POST['rg']
        endereco = request.POST['endereco']
        complemento = request.POST['complemento']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        bairro = request.POST['bairro']
        complemento = request.POST['complemento']
        cep = request.POST['cep']
        telefone = request.POST['telefone']
        data_nascimento = request.POST['data_nascimento']
        nome_mae = request.POST['nome_mae']
        sexo = request.POST['sexo']
        naturalidade = request.POST['naturalidade']
        contato_emergencial = request.POST['contato_emergencial']
        id = request.POST['id']
        print(id)
        if id != 0:
            instance = get_object_or_404(Paciente, id=id)
            form = PacienteForm(request.POST or None, instance=instance)
            form.save()
        else:
            paciente = Paciente.objects.create(email=email, cpf=cpf, nome_paciente=nome_paciente, rg=rg, endereco=endereco, complemento=complemento, cidade=cidade, estado=estado, bairro=bairro, cep=cep, 
            telefone=telefone, data_nascimento=data_nascimento, nome_mae=nome_mae, sexo=sexo, naturalidade=naturalidade, contato_emergencial=contato_emergencial)
            paciente.save()
            print('Paciente cadastrado com sucesso')
        return redirect('index')
    else:
        nome = request.user.username
        id = request.user.id
        #user = User.objects.filter(username=id_user).values_list('usernasme', flat=True)[0]
        pacientes = Paciente.objects.values_list('nome_paciente', flat=True)
        if nome in pacientes:
            paciente = list(Paciente.objects.filter(nome_paciente=nome).values_list()[0])
            return render(request, 'paciente/paciente.html', {'paciente': paciente, 'id': id})
        return render(request, 'paciente/paciente.html', {'id': 0})