from django.contrib import admin
from .models import Categoria, Transacao
from django.db.models import Sum, F
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao','unidades', 'data', 'valor','observacoes','categorias',)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dt_criacao', 'calcular_saldo')
    
    def calcular_saldo(self, obj):
        # Calcula o saldo atual da categoria
        total_depositado = obj.transacao_set.filter(valor__gt=0).aggregate(total=Sum('valor'))['total'] or 0
        total_retirado = obj.transacao_set.filter(valor__lt=0).aggregate(total=Sum(F('valor') * -1))['total'] or 0
        saldo_atual = total_depositado - total_retirado
        return saldo_atual

    calcular_saldo.short_description = 'Saldo Atual'  # Define o nome exibido para o campo de saldo


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Transacao, ProdutoAdmin)