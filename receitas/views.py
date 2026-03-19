from django.shortcuts import render
from django.utils import timezone
from .models import Receita

def home(request):
    return render(request, 'receitas/home.html', {})

def meu_livro_receitas(request):
    meulivro= Receita.objects.filter(author=request.user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'receitas/meu_livro_receitas.html', {'meulivro': meulivro})

def livros_comunidade(request):
    return render(request, 'receitas/livros_comunidade.html', {})

def criar_receita(request):
    return render(request, 'receitas/criar_receita.html',{})