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
    foto_autor = models.ImageField(upload_to='autores', default='autores/default.jpg')
    
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
    foto_editora = models.ImageField(upload_to='editoras', default='editoras/default.jpg')

    def __str__(self):
        return f'Editora: {self.nome} CNPJ: {self.cnpj} Última Modificação: {self.data_ultima_atualizacao}'