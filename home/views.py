from django.shortcuts import render,redirect
from .models import Medicos
from .forms import MedicosForm  

def index(request):
    return render(request,'index.html')

def areapaciente(request):
    return render(request, 'areapaciente.html')

#chama os médicos do banco para retornar na página
def medico(request):
    medico = Medicos.objects.all()
    return render(request, 'medicos.html')

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


