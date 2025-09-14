from django.urls import path
from .views import home, buscar , perfilmusica

urlpatterns = [
    path('',home,name = 'url_home'),
    path('busca/',buscar,name='url_buscar'),
    path('music/<int:pk>',perfilmusica, name='url_perfil'),
]