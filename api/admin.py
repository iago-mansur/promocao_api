from django.contrib import admin
from .models import Promocao, Empresa, Loja

admin.site.register(Loja)
admin.site.register(Empresa)

@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'loja')
