from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import auth

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
        email_digitado = request.POST['email']
        senha_digitada = request.POST['senha']

        if email_digitado == "" or senha_digitada == "":
            print('Os campos email e senha não poddem ficar em branco')
            return redirect('login')
        print(email_digitado, senha_digitada)

        if User.objects.filter(email = email_digitado).exists():
            #email1 = User.objects.filter(email=email_digitado).values_list('email', flat=True)
            user = auth.authenticate(request, email=email_digitado, password=senha_digitada)
            print("Usuario: ", user)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')

        print("Nao foi autenticado. ")
        return redirect('login')
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
