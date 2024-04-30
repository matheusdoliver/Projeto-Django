from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
     
class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    unidades = models.IntegerField(default=0)  # Inicialmente, o contador é definido como 0
    valor = models.DecimalField(max_digits=7, decimal_places=2) #Número máximo de digitos 7 e apenas 2 casas decimais
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE) #Foreignkey faz a transação dessa class com a class Categoria, é obrigatório passar o on_delete.
    observacoes = models.TextField(null=True, blank=True) #Assim não fica obrigatorio descrever o campo
    

    class Meta:
        verbose_name_plural = 'Transação'

    def __str__(self):
        return self.descricao
    
