from django.db import models

class Ingrediente(models.Model):
    UNIDADE_MEDIDA_CHOICES= (
        ("G", "Gramas"),
        ("ML", "Mililítros"),
        ("UN", "unidades")
    )
    nomeingrediente= models.CharField(max_length=128)
    tipo_unidade= models.CharField(max_length=2, choices=UNIDADE_MEDIDA_CHOICES, blank=False, null=False)
    observacoes=models.TextField(blank=True)
    unidade_usada= models.IntegerField(default=1,)
    calorias_unidade=models.IntegerField(default=0)
    
    @property
    def total_calorias_ingrediente(self):
        if self.tipo_unidade=="UN":
            return self.unidade_usada * self.calorias_unidade
        else:
            return self.calorias_unidade
        


class Receita(models.Model):
    nomereceita=models.CharField(max_length=128)
    ingredientes=models.ManyToManyField(Ingrediente)
    modo_de_preparo= models.TextField(blank=True)
    
    @property
    def calorias_total_receita(self):
        return sum(ing.total_calorias_ingrediente for ing in self.ingredientes.all())


    # Create your models here.
