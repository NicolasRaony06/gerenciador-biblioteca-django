from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros, name="livros"),
    path('autor_cadastro/', views.autor_cadastro, name="autor_cadastro"),
]