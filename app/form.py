from django import forms
from .models import Avaliacao
class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(max_length= 100)

class Estrelas(forms.ModelForm):
    model = Avaliacao
    fields = ['estrelas','descricao']
