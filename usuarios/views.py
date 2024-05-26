from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import add_message, constants


def cadastro_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro_usuario.html')
    elif request.method == 'POST':
        username = str(request.POST.get('user')).title().lstrip()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            add_message(request, constants.WARNING, 'A senhas devem ser iguais!')
            return redirect("/usuarios/cadastro_usuario/")
        
        if len(senha) < 8:
            add_message(request, constants.WARNING, 'A senha deve ter pelo menos 8 caracteres!')
            return redirect("/usuarios/cadastro_usuario/")
        
        print(username)

        users_name = User.objects.filter(username=username)

        if users_name.exists():
            add_message(request, constants.ERROR, f'O usuário {username} já existe!')
            return redirect("/usuarios/cadastro_usuario/")
        
        users_email = User.objects.filter(email=email)

        if users_email.exists():
            add_message(request, constants.ERROR, f'O email {email} já existe!')
            return redirect("/usuarios/cadastro_usuario/")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso!')
        return redirect('/usuarios/login/')

def login(request):
    if request.user.username:
        print(request.user.username)
        add_message(request, constants.INFO, 'Você já está logado!')
        return redirect('/')

    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            add_message(request, constants.SUCCESS, 'Logado com sucesso!')
            return redirect('/')
        
        add_message(request, constants.ERROR, 'Usuário ou senha, errados!')
        return redirect('/usuarios/login')

def logout(request):
    auth.logout(request)

    return redirect('/usuarios/login')