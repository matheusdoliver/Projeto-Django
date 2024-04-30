from django.contrib import admin
from .models import Categoria, Transacao
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'valor','observacoes','categorias')


admin.site.register(Categoria)
admin.site.register(Transacao, ProdutoAdmin)