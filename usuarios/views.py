from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import auth
from consulta.models import Consulta

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('O campo não pode ficar em branco')
            return redirect('cadastro')

        if not email.strip():
            print('O campo não pode ficar em branco')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email = email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
            
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        print('Usuário cadastrado com sucesso')
        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Os campos email e senha não poddem ficar em branco')
            return redirect('login')
        print(email, senha)

        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True)[0]
            user = auth.authenticate(request, username=nome, password=senha)
            print(user)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')

        return redirect('login')
    return render(request, 'usuarios/login.html')

    
def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')
        #return render(request, 'usuarios/dashboard.html')

def historicopaciente(request):
    consulta = Consulta.objects.all()
    return render(request, 'usuarios/historicopaciente.html', {'consulta':consulta })