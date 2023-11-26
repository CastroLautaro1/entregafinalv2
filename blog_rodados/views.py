from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from blog_rodados.forms import AutoFormulario
from blog_rodados.models import Articulo, Compacto, SUV, Sedan, PickUp

# Create your views here.

def listar_autos(request):
    contexto = {
        "compacto": Compacto.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='blog_rodados/lista_autos.html',
        context=contexto,
    )
    return http_response

def probando(request):
    contexto = {
        "sedan": Sedan.objects.all()
    }
    http_response = render (
        request=request,
        template_name='blog_rodados/probando.html',
        context=contexto
    )
    return http_response