from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def pagina_inicial(request):
    return render(request, 'home.html')