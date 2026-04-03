from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        # Não incluímos 'author' e 'published_date' pois vamos preencher via código
        fields = ['nomereceita', 'ingredientes', 'modo_de_preparo', 'receita_imagem']
        widgets = {
            'ingredientes': forms.CheckboxSelectMultiple(), # Transforma em lista de seleção
        }