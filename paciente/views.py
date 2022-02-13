# Create your views here.
from django.shortcuts import render,redirect
from .models import Paciente
from .forms import PacienteForm


# def form_view(request):
#     form = PacienteForm()
#     if request.method == 'POST':
#         form = PacienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     return render(request,'sobre.html',{'form':form})


# from django.shortcuts import render
# from .forms import InputForm
 
# # Create your views here.
# def home_view(request):
#     context ={}
#     context['form']= InputForm()
#     return render(request, "home.html", context)