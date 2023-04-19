from django.shortcuts import render
from .models import Notificacoes, Pedidos


def dashboard(request):
    plans = Notificacoes.objects.all()
    p = Pedidos.objects.all()

    dados ={
        'notificacoes':plans,
        'pedido':p
    }


    return render(request, 'home/home.html', dados)
