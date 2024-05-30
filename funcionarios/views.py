from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import add_message, constants
from .models import DadosFuncionario, is_funcionario
from usuarios.views import login
from usuarios.models import is_logado

def home(request):
    #TODO por enquanto não há a verificação se o usuário é um funcionário e pode entrar nesta página.
    if not is_funcionario(request):
        add_message(request, constants.WARNING, "Você não é um funcionário!")
        return redirect('../../')

    if request.method == 'GET':
        return render(request, 'home_funcionario.html')

def cadastro_funcionario(request):
    # TODO verificar se o usuário já está cadastrado como funcionário.
    if not is_logado(request):
        add_message(request, constants.ERROR, 'Você deve estar logado para se tornar um funcionário!')
        return redirect(login)
    
    if is_funcionario(request):
        add_message(request, constants.WARNING, 'Você já é um funcionário!')
        return redirect(home)

    if request.method == 'GET':
        return render(request, 'cadastro_funcionario.html')
    
    elif request.method == 'POST':
        #TODO fazer as variáveis e cadastrar na tabela correta.
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')
        genero = request.POST.get('genero')
        foto_perfil = request.FILES.get('foto_perfil')

        DadosFuncionario.objects.create(
            user = request.user,
            nome_funcionario = nome,
            cpf = cpf,
            data_nascimento = data_nascimento,
            telefone = telefone,
            genero = genero,
            foto_perfil = foto_perfil
        )

        add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso!')
        return redirect(home)