from django.contrib import admin
from .models import Medicos

#Define como será a exibição dos cadastro de médicos na tela de admin
class ListandoMedicos(admin.ModelAdmin):
    #Para exibir mais informações, basta acrescentar ou retirar os campos
    #O nome deve ser o mesmo que o que está em models.py
    list_display = ('id', 'nome_medico', 'especialidade')
    
    #Define os campos clicáveis no admin 
    list_display_links = ('id', 'nome_medico')

    #Cria um campo para busca no admin 
    search_fields = ('nome_medico',)

    #Cria um filtro para especialidade dos médicos
    list_filter = ('especialidade',)
    #O campos "list_filter" e "search_fields" requerem uma tupla como parâmetro, por isso uma vírgula ao final de cada campo 
    #Define quantos médicos serão exibidos por página
    list_per_page = 5

#Medicos = classe de médicos no models
#ListandoMedicos = classe de visualização acima
admin.site.register(Medicos, ListandoMedicos)
