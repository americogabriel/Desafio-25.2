from django.urls import path
from .views import home, buscar

urlpatterns = [
    path('home/',home,name = 'url_home'),
    path('busca/',buscar,name='url_buscar'),
]