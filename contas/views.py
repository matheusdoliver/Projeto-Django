from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
import datetime

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all() #serve para buscar os dados do banco de dados, objetvs é um manage, que vai buscar os dados.
    return render(request,'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return listagem(request)
    
    data['form']= form

    return render(request,'contas/form.html', data)

def home(request):
    return render(request,'contas/index.html')

