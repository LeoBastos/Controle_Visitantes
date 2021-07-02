from django import forms
from django.db.models import fields
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            'nome',
            'cpf',
            'data_Nascimento',
            'numero',
            'placa_veiculo'
        ]
        error_messages = {
            'nome': {
                'required': 'O nome do visitante é obrigatório'
            },
            'cpf': {
                'required': 'O CPF do visitante é obrigatório'
            },
            'data_Nascimento': {
                'required': 'A data de nascimento do visitante é obrigatório',
                'invalid': 'Por Favor, informe um formato de data válido DD/MM/YYYY'
            },
            'numero': {
                'required': 'Informe o numero da Casa'
            },
        }

class AutorizaVisitanteForm(forms.ModelForm):

    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = ['morador_responsavel',]
        error_messages = {
            'morador_responsavel': {
                'required': 'Por favor, informe o nome do morador responsavel por autorizar a entrada do visitante.'
            }
        }