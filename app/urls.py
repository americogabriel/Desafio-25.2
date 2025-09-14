from django.urls import path
from .views import home, buscar , perfilmusica , favoritar , listar , deletar , update

urlpatterns = [
    path('',home,name = 'url_home'),
    path('busca/',buscar,name='url_buscar'),
    path('music/<int:pk>',perfilmusica, name='url_perfil'),
    path('favoritar/<int:pk>',favoritar, name='url_favoritar'),
    path('listar/',listar.as_view(), name='url_listar'),
    path('deletar/<int:pk>',deletar.as_view(), name='url_deletar'),
    path('atualizar/<int:pk>',update.as_view(), name = 'url_atualizar')
]