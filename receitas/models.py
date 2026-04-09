from django.db import models
from django.conf import settings
from django.utils import timezone

class Ingrediente(models.Model):
    UNIDADE_MEDIDA_CHOICES= (
        ("G", "Gramas"),
        ("ML", "Mililítros"),
        ("UN", "unidades")
    )
    nomeingrediente= models.CharField("Nome Do Ingrediente", max_length=128)
    tipo_unidade= models.CharField("Tipo De unidade", max_length=2, choices=UNIDADE_MEDIDA_CHOICES, blank=False, null=False)
    observacoes=models.TextField(blank=True)
    unidade_usada= models.IntegerField(default=1,)
    calorias_unidade=models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    ingrediente_imagem= models.ImageField("imagem do ingrediente", null=True, blank=True, upload_to="images/")
    
    @property
    def total_calorias_ingrediente(self):
        if self.tipo_unidade=="UN":
            return self.unidade_usada * self.calorias_unidade
        else:
            return self.calorias_unidade
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.nomeingrediente

        


class Receita(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_da_receita=models.CharField(max_length=128)
    ingredientes=models.ManyToManyField(Ingrediente)
    modo_de_preparo= models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    receita_imagem= models.ImageField(null=True, blank=True, upload_to="images/")
   
    @property
    def calorias_total_receita(self):
        return sum(ing.total_calorias_ingrediente for ing in self.ingredientes.all())
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.nome_da_receita



    # Create your models here.
