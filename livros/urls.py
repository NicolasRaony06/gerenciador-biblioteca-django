from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros, name="livros"),
    path('autor_cadastro/', views.autor_cadastro, name="autor_cadastro"),
    path('visualizar_autores/', views.visualizar_autores, name="visualizar_autores"),
    path('alterar_autor/<int:id>/', views.alterar_autor, name="alterar_autor"),
    path('excluir_autor/<int:id>/', views.excluir_autor, name="excluir_autor"),
]