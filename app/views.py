from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .form import PesquisaForm
import requests

def home(request):
    data = {}
    data['form'] = PesquisaForm
    return render(request,'app/home.html',data)

def buscar(request):
    query = request.POST.get('pesquisa')
    response = requests.get(f"https://api.deezer.com/search?q={query}")
    banco = {}
    banco['dados'] = response.json()
    return render(request,'app/musicas.html',banco)





