from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_funcionario'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario')
]
