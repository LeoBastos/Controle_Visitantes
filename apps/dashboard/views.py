from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from visitantes.models import Visitante
from django.utils import timezone


@login_required
def index(request):
    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    visitantes = Visitante.objects.order_by('-horario_chegada')

    visitantes_aguardando = visitantes.filter(status='AGUARDANDO')
    visitantes_em_visita = visitantes.filter(status='EM_VISITA')
    visitantes_finalizado = visitantes.filter(status='FINALIZADO')    
    visitantes_mes = visitantes.filter(horario_chegada__month=mes_atual)
    
    context = {
        'nome_pagina': 'Dashboard',
        'visitantes': visitantes,
        'visitantes_aguardando': visitantes_aguardando.count(),
        'visitantes_em_visita': visitantes_em_visita.count(),
        'visitantes_finalizado': visitantes_finalizado.count(),
        'visitantes_mes': visitantes_mes.count()
    }

    return render(request, 'index.html', context)


