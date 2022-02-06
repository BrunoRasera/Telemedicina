from django.contrib import admin

from consulta.models import Consulta
from .models import Feedback_consulta

class ListandoFeedbackConsulta(admin.ModelAdmin):
    #Para exibir mais informações, basta acrescentar ou retirar os campos
    #O nome deve ser o mesmo que o que está em models.py
    list_display = ('id',)

admin.site.register(Feedback_consulta, ListandoFeedbackConsulta)
