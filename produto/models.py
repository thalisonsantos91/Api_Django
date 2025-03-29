from django.db import models
from categoria.models import categoria

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='produtos')

    class Meta:
        db_table = "produto"

    def __str__(self):
        return self.nome