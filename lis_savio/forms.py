from django import forms
from .models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'categoria', 'imagem']

