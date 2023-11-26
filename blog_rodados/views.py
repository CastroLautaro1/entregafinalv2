from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from blog_rodados.forms import AutoFormulario
from blog_rodados.models import Articulo, Compacto, SUV, Sedan, PickUp

# Create your views here.

def listar_compactos(request):
    contexto = {
        "compacto": Compacto.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='blog_rodados/lista_compacto.html',
        context=contexto,
    )
    return http_response

def listar_sedanes(request):
    contexto = {
        "sedan": Sedan.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='blog_rodados/lista_sedan.html',
        context=contexto,
    )
    return http_response

def listar_suv(request):
    contexto = {
        "suv": SUV.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='blog_rodados/lista_suv.html',
        context=contexto,
    )
    return http_response

def listar_pickup(request):
    contexto = {
        "pickup": PickUp.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='blog_rodados/lista_pickup.html',
        context=contexto,
    )
    return http_response

def modelos(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='blog_rodados/modelos.html',
        context=contexto,
    )
    return http_response



