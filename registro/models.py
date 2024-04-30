from django.db import models

class computador(models.Model):
    nome = models.CharField(max_length=100)
    data_entrada = models.DateField()
    data_entrega = models.DateField()

    def __str__(self):
        return self.nome
