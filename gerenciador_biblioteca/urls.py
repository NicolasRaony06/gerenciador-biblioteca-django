from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from funcionarios.models import is_funcionario

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: render(request, 'home.html', {'is_funcionario': is_funcionario(request)}), name="home"),
    path("usuarios/", include('usuarios.urls')),
    path("funcionarios/", include('funcionarios.urls')),
    path("livros/", include('livros.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
