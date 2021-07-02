from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from visitantes.models import Visitante
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm
from django.utils import timezone
from django.http import HttpResponseNotAllowed


@login_required
def registrar_visitante(request):
    form = VisitanteForm()

    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()
            messages.success(request, 'Visistante Registrado com Sucesso.')

            return redirect('index')

    context = {
        'title': 'Registrar Visitante',
        'form': form
    }
    return render(request, 'registrar_visitante.html', context)


@login_required
def buscar_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    
    form = AutorizaVisitanteForm()
    if request.method == 'POST':
        form = AutorizaVisitanteForm(request.POST, instance=visitante)
        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.status = 'EM_VISITA'
            visitante.horario_autorizacao = timezone.now()
            visitante.save()

            messages.success(request,'Entrada de visitante autorizada com sucesso.')
            
            return redirect('index')
    
    context = {
        'title': 'Informação de Visitante',
        'visitante': visitante,
        'form': form,
    }

    return render(request, 'informacoes_visitante.html', context)


@login_required
def finalizar_visita(request, id):
    if request.method == 'POST':
        visitante = get_object_or_404(Visitante, id=id)
        
        visitante.status = 'FINALIZADO'
        visitante.horario_saida = timezone.now()
        
        visitante.save()
        
        messages.success(request, 'Visita Finalizada')

        return redirect('index')
    
    else:
        return HttpResponseNotAllowed(['POST'], 'Método não Permitido')