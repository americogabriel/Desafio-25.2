from django import forms

class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(max_length= 100)
