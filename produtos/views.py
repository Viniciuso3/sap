from django.shortcuts import render
from .models import Lista_produtos, Categoria_p

def produtos(request):
    produto = Lista_produtos.objects.all()
    tp = Categoria_p.objects.all()

    dados ={
        'lista': produto,
        'p' : tp
    }

    return render(request, 'produtos/produtos.html', dados)
