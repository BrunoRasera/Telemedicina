from django.shortcuts import render,redirect
from .models import Medicos
from .forms import MedicosForm  

def index(request):
    return render(request,'index.html')

def cadastromedico(request):
    return render(request, 'cadastromedico.html')

def areapaciente(request):
    return render(request, 'areapaciente.html')

#chama os médicos do banco para retornar na página
def medico(request):
    medico = Medicos.objects.all()
    return render(request, 'medicos.html')

def form_view(request):
    form = MedicosForm()
    if request.method == 'POST':
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'cadastromedico.html',{'form':form})



