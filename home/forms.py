from django import forms
from .models import Medicos

class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = '__all__'
