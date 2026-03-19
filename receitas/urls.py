from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meu_livro_receitas', views.meu_livro_receitas, name='meu_livro'),
    path('livros_comunidade', views.livros_comunidade, name='livros_comunidade'),
    path('criar_receita', views.criar_receita, name='criar_receita' )
]