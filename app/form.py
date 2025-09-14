from django import forms
from .models import Avaliacao


class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(max_length= 100)

class AtualizarForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nomemusica','estrelas','descricao']
    
