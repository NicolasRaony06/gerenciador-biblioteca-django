from django.shortcuts import render, HttpResponse, redirect
from .models import Autor
from funcionarios.models import is_funcionario, DadosFuncionario
from django.contrib.messages import add_message, constants

def livros(request):
    return HttpResponse("Em desenvolvimento...")

def autor_cadastro(request):
    if not is_funcionario(request):
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect("/")
    
    if request.method == "GET":
        return render(request, 'autor_cadastro.html')
    
    if request.method == "POST":
        nome = str(request.POST.get('nome')).title().lstrip()
        genero = request.POST.get('genero')
        biografia = request.POST.get('biografia')
        nacionalidade = request.POST.get('nacionalidade')
        data_nascimento = request.POST.get('data_nascimento')

        funcionario = DadosFuncionario.objects.get(user=request.user)

        if not Autor.objects.filter(nome=nome):

            autor = Autor(
                nome = nome,
                genero = genero,
                biografia = biografia,
                nacionalidade = nacionalidade,
                data_nascimento = data_nascimento,
                funcionario = funcionario
            )

            autor.save()

            add_message(request, constants.SUCCESS, "Autor cadastrado com sucesso!")
            return redirect("/funcionarios/home")
        
        add_message(request, constants.ERROR, f"O Autor(a) {nome} já existe")
        return redirect(autor_cadastro)
    
def visualizar_autores(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        return render(request, 'visualizar_autores.html', {'autores': autores})
