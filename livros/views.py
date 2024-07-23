from django.shortcuts import render, HttpResponse, redirect
from .models import Autor, Editora
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
        foto_autor = request.FILES.get('foto_autor')

        funcionario = DadosFuncionario.objects.get(user=request.user)

        if not Autor.objects.filter(nome=nome):

            autor = Autor(
                nome = nome,
                genero = genero,
                biografia = biografia,
                nacionalidade = nacionalidade,
                data_nascimento = data_nascimento,
                funcionario = funcionario,
                foto_autor = foto_autor,
            )

            autor.save()

            add_message(request, constants.SUCCESS, "Autor cadastrado com sucesso!")
            return redirect("/funcionarios/home")
        
        add_message(request, constants.ERROR, f"O Autor(a) {nome} já existe")
        return redirect(autor_cadastro)
    
def visualizar_autores(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        return render(request, 'visualizar_autores.html', {'autores': autores, 'is_funcionario': is_funcionario(request)})

def alterar_autor(request, id):
    if not request.user.is_funcionario:
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_autores)
    
    if request.method == 'GET':
        try:
            autor = Autor.objects.get(id=id)
        except:
            add_message(request, constants.ERROR, 'Id de autor inválido!')
            return redirect(visualizar_autores)
        
        return render(request, 'alterar_autor.html', {'autor': autor})

    if request.method == 'POST':
        try:
            autor = Autor.objects.get(id=id)

            nome = str(request.POST.get('nome')).title().lstrip() if request.POST.get('nome') else autor.nome
            genero = request.POST.get('genero') if request.POST.get('genero') else autor.genero
            biografia = request.POST.get('biografia') if request.POST.get('biografia') else autor.biografia
            nacionalidade = request.POST.get('nacionalidade') if request.POST.get('nacionalidade') else autor.nacionalidade
            data_nascimento = request.POST.get('data_nascimento') if request.POST.get('data_nascimento') else autor.data_nascimento
            foto_autor = request.FILES.get('foto_autor') if request.FILES.get('foto_autor') else autor.foto_autor

            funcionario = DadosFuncionario.objects.get(user=request.user)

            autor.nome = nome
            autor.genero = genero
            autor.biografia = biografia
            autor.nacionalidade = nacionalidade
            autor.data_nascimento = data_nascimento
            autor.foto_autor = foto_autor
            autor.funcionario = funcionario

            autor.save()

        except:
            add_message(request, constants.ERROR, "Erro ao tentar alterar autor!")
            return redirect(visualizar_autores)
        
        add_message(request, constants.SUCCESS, "Autor alterado com sucesso!")
        return redirect(visualizar_autores)

def excluir_autor(request, id):
    if not request.user.is_funcionario:
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_autores)

    if request.method == 'GET':
        try:
            autor = Autor.objects.get(id=id)
            autor.delete()
        except:
            add_message(request, constants.ERROR, "Erro ao tentar excluir autor(a)!")
            return redirect(visualizar_autores)
        
        add_message(request, constants.SUCCESS, "Autor(a) excluído com sucesso!")
        return redirect(visualizar_autores)
    
def editora_cadastro(request):
    if not request.user.is_funcionario:
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    if request.method == 'GET':
        return render(request, 'editora_cadastro.html')
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        site = request.POST.get('site')
        descricao = request.POST.get('descricao')
        foto_editora = request.FILES.get('foto_editora')
        funcionario = DadosFuncionario.objects.get(user=request.user)

        if Editora.objects.filter(cnpj=cnpj) or Editora.objects.filter(email=email):
            add_message(request, constants.ERROR, f"A Editora {nome} com o CNPJ {cnpj} e Email {email} já existe!")
            return redirect(editora_cadastro)
        
        try:
            editora = Editora(
                nome=nome,
                cnpj=cnpj,
                endereco=endereco,
                telefone=telefone,
                email=email,
                site=site,
                descricao=descricao,
                foto_editora=foto_editora,
                funcionario=funcionario,
            )

            editora.save()

            add_message(request, constants.SUCCESS, "Editora cadastrada com sucesso!")
            return redirect(visualizar_editoras)

        except:
            add_message(request, constants.ERROR, "Erro ao tentar cadastrar um nova Editora!")
            return redirect(editora_cadastro)
        
def visualizar_editoras(request):
    if not request.user.is_funcionario:
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    if request.method == 'GET':
        return redirect(visualizar_autores)

def alterar_editora(request):
    if not request.user.is_funcionario:
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    if request.method == 'GET':
        pass

def excluir_editora(request):
    if not request.user.is_funcionario:
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    if request.method == 'GET':
        pass