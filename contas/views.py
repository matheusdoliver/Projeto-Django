from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
import datetime

def home(request):
    return render(request,'contas/index.html')

