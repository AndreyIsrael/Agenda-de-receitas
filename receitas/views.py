from django.shortcuts import render
from django.utils import timezone
from .models import Receita, Ingrediente
from .forms import ReceitaForm, IngredienteForm
from django.shortcuts import render, redirect
def home(request):
    return render(request, 'receitas/home.html', {})

def meu_livro_receitas(request):
    meulivro= Receita.objects.filter(author=request.user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'receitas/meu_livro_receitas.html', {'meulivro': meulivro})

def livros_comunidade(request):
    receitasall= Receita.objects.filter( published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'receitas/livros_comunidade.html', {'receitasall':receitasall})

def criar_receita(request):
    if request.method == "POST":
            form =ReceitaForm(request.POST, request.FILES)
            if form.is_valid():
                 receita = form.save(commit=False)
                 receita.author = request.user 
                 receita.save()
                 form.save_m2m() 
                 return redirect('/')
    else:
        form=ReceitaForm()

    return render(request, 'receitas/criar_receita.html',{'form':form})


def criar_ingrediente(request):
    if request.method == "POST":
         form = IngredienteForm(request.POST, request.FILES)
         if form.is_valid():
              form.save()
              return redirect('/criar_receita')
         
    else:
         form=IngredienteForm()
          
    return render(request, 'receitas/criar_ingrediente.html',{'form':form})

