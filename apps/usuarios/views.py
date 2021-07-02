from django.shortcuts import render
from visitantes.models import Visitante


def index(request):
    visitantes = Visitante.objects.all()
    context = {
        'nome_pagina': 'Dashboard',
        'visitantes': visitantes,
    }
    return render(request, 'index.html', context)


