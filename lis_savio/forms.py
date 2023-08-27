# Importando o módulo forms do Django
from django import forms
# Importando o modelo Treino definido em models.py
from .models import Treino

# Definindo uma classe de formulário chamada TreinoForm
class TreinoForm(forms.ModelForm):
    # Classe Meta é usada para configurar metadados do formulário
    class Meta:
        # Especificando o modelo associado a este formulário (Treino)
        model = Treino
        # Especificando quais campos do modelo serão incluídos no formulário
        fields = ['nome', 'categoria', 'imagem']

