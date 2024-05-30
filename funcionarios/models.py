from django.db import models
from django.contrib.auth.models import User

def is_funcionario(request):
    if DadosFuncionario.objects.filter(user=request.user):
        return True

class DadosFuncionario(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_funcionario = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    data_ingressao = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=15)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    foto_perfil = models.ImageField(upload_to='fotos_perfil')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


