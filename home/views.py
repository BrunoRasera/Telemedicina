from django.shortcuts import render,redirect
from .models import Medicos
from .forms import MedicosForm  

def index(request):
    return render(request,'index.html')

def areapaciente(request):
    return render(request, 'areapaciente.html')

#chama os médicos do banco para retornar na página
#def medico(request):
#    medico = Medicos.objects.all()
#    return render(request, 'medicos.html')

def areamedico(request):
    form = MedicosForm()
    if request.method == 'POST':
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'areamedico.html',{'form':form})


def consulta(request):
    # Get all
    med = Medicos.objects.all()
    #med = Medicos.objects.get()
    print("Myoutput",med)
    return render(request,'consulta.html',{'med': med})

def medico(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        nome_medico = request.POST['nome_medico']
        rg = request.POST['rg']
        crm = request.POST['crm']
        especialidade = request.POST['especialidade']
        area_atuacao = request.POST['area_atuacao']
        endereco = request.POST['endereco']
        complemento = request.POST['complemento']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        bairro = request.POST['bairro']
        complemento = request.POST['complemento']
        cep = request.POST['cep']
        telefone = request.POST['telefone']
        data_nascimento = request.POST['data_nascimento']
        print(rg, cpf)
        medico = Medicos.objects.create(cpf=cpf, nome_medico=nome_medico, rg=rg, endereco=endereco, complemento=complemento, cidade=cidade, estado=estado, bairro=bairro, cep=cep, 
        telefone=telefone, data_nascimento=data_nascimento, especialidade=especialidade, area_atuacao=area_atuacao, crm=crm)
        medico.save()

        print('Medico cadastrado com sucesso')
        return redirect('index')

    return render(request, 'medico/medico.html')
