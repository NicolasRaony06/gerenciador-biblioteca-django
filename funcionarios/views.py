from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    #TODO por enquanto não há a verificação se o usuário é um funcionário e pode entrar nesta página.
    if request.method == 'GET':
        return render(request, 'home_funcionario.html')

def cadastro_funcionario(request):
    # TODO verificar se o usuário já está cadastrado como funcionário.
    if request.method == 'GET':
        return HttpResponse("Página em criação!")
    
    if render.method == 'POST':
        #TODO fazer as variáveis e cadastrar na tabela correta.
        return HttpResponse("Página em criação!")