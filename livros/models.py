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
    funcionario = models.ForeignKey(DadosFuncionario, on_delete=models.DO_NOTHING)
    foto_autor = models.ImageField(upload_to='autores', default='autores/default.jpg')

    def __str__(self):
        return self.nome