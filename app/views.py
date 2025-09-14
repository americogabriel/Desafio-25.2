from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .form import PesquisaForm , AtualizarForm
import requests
from .models import Avaliacao, Favoritas
from django.views.generic import ListView, UpdateView , DeleteView
from django.urls import reverse_lazy

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

def perfilmusica(request,pk):
    if request.method == 'POST':
        nome = request.POST.get('nome_musica')
        estrelas = request.POST.get('estrelas')
        opniao = request.POST.get('opniao')
        create = Avaliacao.objects.create(estrelas = estrelas, descricao = opniao, nomemusica = nome)
    response = requests.get(f'https://api.deezer.com/track/{pk}')
    banco = {}
    banco['musica'] = response.json()
    return render(request,'app/perfil.html',banco)


def favoritar(request,pk):
    checkbox = request.POST.get('favorito')
    if checkbox:
        response = requests.get(f'https://api.deezer.com/track/{pk}')
        banco = {}
        banco['musica'] = response.json()
        data = response.json()
        nomemusica = data['title']
        nomeartista = data['artist']['name']
        create = Favoritas.objects.create(artista = nomeartista, musica= nomemusica)
        return render(request,'app/perfil.html',banco)
    else:
        response = requests.get(f'https://api.deezer.com/track/{pk}')
        banco = {}
        banco['musica'] = response.json()
        return render(request,'app/perfil.html',banco)

class listar(ListView):
    model = Avaliacao
    template_name = 'app/avaliacaolist.html'
    context_object_name = 'avaliacoes'

class listarfavoritas(ListView):
    model = Favoritas
    template_name = 'app/listarfavoritas.html'
    context_object_name = 'favoritas'

class deletar(DeleteView):
    model = Avaliacao
    template_name = 'app/remover.html'
    context_object_name = 'avaliacao'
    success_url = reverse_lazy('url_listar')

class update(UpdateView):
    model = Avaliacao
    template_name = 'app/update.html'
    form_class = AtualizarForm
    success_url = reverse_lazy('url_listar')





    


