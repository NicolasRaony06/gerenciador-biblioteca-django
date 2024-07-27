from django.db import models
from funcionarios.models import DadosFuncionario

class Autor(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]

    nome = models.CharField(max_length=80, null=False)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, default='O')
    biografia = models.TextField(null=False)
    nacionalidade = models.CharField(max_length=30, null=False)
    data_nascimento = models.DateField(null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    funcionario = models.ForeignKey(DadosFuncionario, on_delete=models.DO_NOTHING)
    foto_autor = models.ImageField(upload_to='autores')
    
    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=250, null=False)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    site = models.URLField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    funcionario = models.ForeignKey(DadosFuncionario, on_delete=models.DO_NOTHING)
    foto_editora = models.ImageField(upload_to='editoras')

    def __str__(self):
        return f'Editora: {self.nome} CNPJ: {self.cnpj} Última Modificação: {self.data_ultima_atualizacao}'

class Genero(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Livro(models.Model): #TODO adicionar genero do livro
    titulo = models.CharField(max_length=150, null=False, blank=False)
    isbn = models.CharField(max_length=20, unique=True, null=False)
    generos = models.ManyToManyField(Genero, related_name='livros')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    data_publicacao = models.DateField(null=False)
    numero_paginas = models.PositiveIntegerField(null=False)
    numero_amostras = models.PositiveIntegerField(null=False)
    descricao = models.TextField(blank=True)
    capa = models.ImageField(upload_to='livros_capas')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    funcionario = models.ForeignKey(DadosFuncionario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Livro: {self.titulo} Autor(a): {self.autor.nome} Editora: {self.editora.nome}'

