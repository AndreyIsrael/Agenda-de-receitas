from django.shortcuts import render
from django.utils import timezone,reverse_lazy 
from .models import Receita
from .forms import ReceitaForm
from django.views.generic import ListView,DetailView, CreateView

def home(request):
    return render(request, 'receitas/home.html', {})

def meu_livro_receitas(request):
    meulivro= Receita.objects.filter(author=request.user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'receitas/meu_livro_receitas.html', {'meulivro': meulivro})

def livros_comunidade(request):
    return render(request, 'receitas/livros_comunidade.html', {})

class AdicionarReceitaView(CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'criar_receita.html'
    success_url = reverse_lazy('sua_url_de_sucesso') # Ex: 'meu_livro'

    def form_valid(self, form):
        # O autor precisa ser o usuário logado
        form.instance.author = self.request.user
        return super().form_valid(form)