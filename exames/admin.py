from django.contrib import admin
from .models import Exame

class ListandoExame(admin.ModelAdmin):
    #Para exibir mais informações, basta acrescentar ou retirar os campos
    #O nome deve ser o mesmo que o que está em models.py
    list_display = ('id',)

admin.site.register(Exame, ListandoExame)
