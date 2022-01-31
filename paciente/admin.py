from django.contrib import admin
from .models import Paciente

class ListandoPacientes(admin.ModelAdmin):
    list_display = ('id', 'nome_paciente', 'email')
    list_display_links = ('id', 'nome_paciente')
    search_fields = ('nome_paciente',)
    list_per_page = 5

admin.site.register(Paciente, ListandoPacientes)