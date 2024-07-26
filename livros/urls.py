from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizar_livros, name="visualizar_livros"),
    path('autor_cadastro/', views.autor_cadastro, name="autor_cadastro"),
    path('visualizar_autores/', views.visualizar_autores, name="visualizar_autores"),
    path('alterar_autor/<int:id>/', views.alterar_autor, name="alterar_autor"),
    path('excluir_autor/<int:id>/', views.excluir_autor, name="excluir_autor"),
    path('editora_cadastro/', views.editora_cadastro, name="editora_cadastro"),
    path('visualizar_editoras/', views.visualizar_editoras, name="visualizar_editoras"),
    path('alterar_editora/<int:id>/', views.alterar_editora, name="alterar_editora"),
    path('excluir_editora/<int:id>/', views.excluir_editora, name="excluir_editora"),
    path("visualizar_livros/", views.visualizar_livros, name="visualizar_livros"),
    path("livro_cadastro/", views.livro_cadastro, name="livro_cadastro"),
]