from django.shortcuts import render, HttpResponse, redirect
from .models import Autor, Editora, Livro, Genero
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
        foto_autor = request.FILES.get('foto_autor') if request.FILES.get('foto_autor') else 'autores/default.jpg'

        funcionario = DadosFuncionario.objects.get(user=request.user)

        if not Autor.objects.filter(nome=nome):
            try:    
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
            except:
                add_message(request, constants.ERROR, "Erro ao tentar cadastrar um novo autor!")
                return redirect(autor_cadastro)
        
        add_message(request, constants.ERROR, f"O Autor(a) {nome} já existe")
        return redirect(autor_cadastro)
    
def visualizar_autores(request):
    if request.method == 'GET':
        autores = Autor.objects.all()

        if request.GET.get('nome_autor'):
            autores = autores.filter(nome__icontains=request.GET.get('nome_autor'))

        if request.GET.get('genero'):
            autores = autores.filter(genero=request.GET.get('genero'))

        return render(request, 'visualizar_autores.html', {'autores': autores, 'is_funcionario': is_funcionario(request)})

def alterar_autor(request, id):
    if not is_funcionario(request):
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
    if not is_funcionario(request):
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
    if not is_funcionario(request):
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    if request.method == 'GET':
        return render(request, 'editora_cadastro.html')
    
    if request.method == 'POST':
        nome = str(request.POST.get('nome')).title().lstrip()
        cnpj = request.POST.get('cnpj')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        site = request.POST.get('site')
        descricao = request.POST.get('descricao')
        foto_editora = request.FILES.get('foto_editora') if request.FILES.get('foto_editora') else 'editoras/default.jpg'
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
    if request.method == 'GET':
        editoras = Editora.objects.all()

        if request.GET.get('nome_editora'):
            editoras = editoras.filter(nome__icontains=request.GET.get('nome_editora'))

        return render(request, 'visualizar_editoras.html', {'editoras': editoras, 'is_funcionario': is_funcionario(request)})

def alterar_editora(request, id):
    if not is_funcionario(request):
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    try:
        editora = Editora.objects.get(id=id)
    except:
        add_message(request, constants.ERROR, "ID de editora inválida!")
        return redirect(visualizar_editoras)

    if request.method == 'GET':
        return render(request, 'alterar_editora.html', {'editora': editora})
    
    if request.method == 'POST':
        try:
            nome = str(request.POST.get('nome')).title().lstrip() if request.POST.get('nome') else editora.nome
            cnpj = request.POST.get('cnpj') if request.POST.get('cnpj') else editora.cnpj
            endereco = request.POST.get('endereco') if request.POST.get('endereco') else editora.endereco
            telefone = request.POST.get('telefone') if request.POST.get('telefone') else editora.telefone
            email = request.POST.get('email') if request.POST.get('email') else editora.email
            site = request.POST.get('site') if request.POST.get('site') else editora.site
            descricao = request.POST.get('descricao') if request.POST.get('descricao') else editora.descricao
            foto_editora = request.FILES.get('foto_editora') if request.FILES.get('foto_editora') else editora.foto_editora

            funcionario = DadosFuncionario.objects.get(user=request.user)
            
            editora.nome = nome
            editora.cnpj = cnpj
            editora.endereco = endereco
            editora.telefone = telefone
            editora.email = email
            editora.site = site
            editora.descricao = descricao
            editora.foto_editora = foto_editora
            editora.funcionario = funcionario

            editora.save()

            add_message(request, constants.SUCCESS, f"Editora {nome} alterada com sucesso")
            return redirect(visualizar_editoras)

        except:
            add_message(request, constants.ERROR, f"Erro ao tentar alterar a editora {nome}")
            return redirect(visualizar_editoras)

def excluir_editora(request, id):
    if not is_funcionario(request):
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_editoras)
    
    if request.method == 'GET':
        try:
            editora = Editora.objects.get(id=id)
            editora.delete()

            add_message(request, constants.SUCCESS, "Editora excluida com sucesso!")
            return redirect(visualizar_editoras)
        except:
            add_message(request, constants.ERROR, "Erro ao tentar excluir a editora")
            return redirect(visualizar_editoras)
        
def livro_cadastro(request):
    if not is_funcionario(request):
        add_message(request, constants.WARNING, "Você não é funcionário!")
        return redirect(visualizar_livros)
    
    if request.method == 'GET':
        autores = Autor.objects.all()
        editoras = Editora.objects.all()

        return render(request, "livro_cadastro.html", {'autores': autores, 'editoras': editoras})
    
    if request.method == 'POST':    
        titulo = str(request.POST.get('titulo')).title().lstrip()
        isbn = request.POST.get('isbn')
        generos_ids = request.POST.getlist('generos')
        autor_id = request.POST.get('autor')
        editora_id = request.POST.get('editora')
        data_publicacao = request.POST.get('data_publicacao')
        numero_paginas = request.POST.get('numero_paginas')
        numero_amostras = request.POST.get('numero_amostras') if not request.POST.get('numero_amostras') == str('') else 0
        descricao = request.POST.get('descricao')
        capa = request.FILES.get('capa') if request.FILES.get('capa') else 'livros_capas/default.jpeg'
        funcionario = DadosFuncionario.objects.get(user=request.user)

        if Livro.objects.filter(isbn=isbn):
            add_message(request, constants.ERROR, f"O ISBN {isbn} já está cadastrado!")

            return redirect(livro_cadastro)

        try:
            livro = Livro(
                titulo = titulo,
                isbn = isbn,
                autor = Autor.objects.get(id=autor_id),
                editora = Editora.objects.get(id=editora_id),
                data_publicacao = data_publicacao,
                numero_paginas = numero_paginas,
                numero_amostras = numero_amostras,
                descricao = descricao, 
                capa = capa,
                funcionario = funcionario,
            )

            livro.save()

            for genero_id in generos_ids:
                genero = Genero.objects.get(id=genero_id)
                livro.generos.add(genero)

            add_message(request, constants.SUCCESS, "Livro cadastrado com sucesso!")
            return redirect(visualizar_livros)
        
        except:
            add_message(request, constants.ERROR, "Erro ao tentar cadastrar um novo livro!")
            return redirect(livro_cadastro)

def visualizar_livros(request):
    if request.method == 'GET':
        livros = Livro.objects.all()

        return render(request, 'visualizar_livros.html', {'livros': livros})