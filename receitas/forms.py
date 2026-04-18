from django import forms
from .models import Receita, Ingrediente

class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita
        fields = ("nome_da_receita","ingredientes","modo_de_preparo", "receita_imagem"  )
   
class  IngredienteForm(forms.ModelForm):

    class Meta:
        model= Ingrediente
        fields = ( "nomeingrediente","observacoes", "tipo_unidade", "unidade_usada", "calorias_unidade", "ingrediente_imagem")
