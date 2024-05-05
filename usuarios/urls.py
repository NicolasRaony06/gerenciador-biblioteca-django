from django.urls import path, include
from . import views

urlpatterns = [
    path("cadastro_usuario/", views.cadastro_usuario, name="cadastro_usuario"),
    path("login/", views.login, name="login"),
]
