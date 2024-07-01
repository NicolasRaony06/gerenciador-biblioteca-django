from django.db import models
from funcionarios.models import DadosFuncionario

class Autor(models.Model):
    nome = models.CharField(max_length=80, null=False)
    biografia = models.TextField(null=False)
    nacionalidade = models.CharField(max_length=30, null=False)
    data_nascimento = models.DateField(null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(DadosFuncionario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome