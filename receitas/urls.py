from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meu-livro-receitas', views.meu_livro_receitas, name='meu_livro'),
    path('livros-comunidade', views.livros_comunidade, name='livros_comunidade')
]