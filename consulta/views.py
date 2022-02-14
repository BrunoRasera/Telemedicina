from django.shortcuts import render

# Create your views here.
def pagamentoconsulta(request):
    return render(request, 'consulta/pagamentoconsulta.html')

def visualizaconsulta(request):
    return render(request, 'consulta/visualizaconsulta.html')

def agendaconsulta(request):
    return render(request, 'consulta/agendaconsulta.html')
