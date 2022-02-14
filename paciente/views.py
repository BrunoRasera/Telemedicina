from django.shortcuts import render, redirect
from .models import Paciente

def paciente(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
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
        print(nome_paciente, rg, cpf)
        paciente = Paciente.objects.create(cpf=cpf, nome_paciente=nome_paciente, rg=rg, endereco=endereco, complemento=complemento, cidade=cidade, estado=estado, bairro=bairro, cep=cep, 
        telefone=telefone, data_nascimento=data_nascimento, nome_mae=nome_mae, sexo=sexo, naturalidade=naturalidade, contato_emergencial=contato_emergencial)
        paciente.save()

        print('Paciente cadastrado com sucesso')
        return redirect('index')

    return render(request, 'paciente/paciente.html')