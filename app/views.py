from django.shortcuts import render
from django.http import HttpResponse
from .form import PesquisaForm
import requests

def home(request):
    data = {}
    data['form'] = PesquisaForm
    return render(request,'app/home.html',data)

def buscar(request):
    query = request.POST.get('pesquisa')
    reponse = requests.get(f"https://api.deezer.com/search?q={query}")
    dados = reponse.json()
    return render(request,'app/musicas.html',dados)
