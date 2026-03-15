from django.shortcuts import render

def home(request):
    return render(request, 'receitas/home.html', {})

def meu_livro_receitas(request):
    return render(request, 'receitas/meu-livro-receitas.html', {})

def livros_comunidade(request):
    return render(request, 'receitas/livros-comunidade.html', {})