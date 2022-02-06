from django.contrib import admin

from feedback_consulta.admin import ListandoFeedbackConsulta
from .models import Feedback_medico

class ListandoFeedbackMedico(admin.ModelAdmin):
    #Para exibir mais informações, basta acrescentar ou retirar os campos
    #O nome deve ser o mesmo que o que está em models.py
    list_display = ('id',)

admin.site.register(Feedback_medico, ListandoFeedbackMedico)
