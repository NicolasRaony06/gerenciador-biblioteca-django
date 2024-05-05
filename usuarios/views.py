from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import add_message, constants


def cadastro_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro_usuario.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            add_message(request, constants.WARNING, 'A senhas devem ser iguais!')
            return redirect("/usuarios/cadastro_usuario/")
        
        if len(senha) < 8:
            add_message(request, constants.WARNING, 'A senha deve ter pelo menos 8 caracteres!')
            return redirect("/usuarios/cadastro_usuario/")
        
        users = User.objects.filter(username=user)

        if users.exists():
            add_message(request, constants.ERROR, f'O usuário {user} já existe!')
            return redirect("/usuarios/cadastro_usuario/")

        user = User.objects.create_user(
            username=user,
            email=email,
            password=senha
        )

        add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso!')
        return redirect('/usuarios/login/')

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    