from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "categoria"

    def __str__(self):
        return self.nome