from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from blog_rodados.forms import UserFormulario
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

def listar_articulos(request):
    contexto = {
        "articulo": Articulo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='blog_rodados/plan_pago.html',
        context=contexto,
    )
    return http_response

def agregar_compacto(request, id):
   compacto = Compacto.objects.get(id=id)
   if request.method == "POST":
       formulario = UserFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           compacto.modelo = data['modelo']
           compacto.anio = data['anio']
           compacto.save()
           url_exitosa = reverse('auto_compacto')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'anio': compacto.anio,
           'anio': compacto.anio,
       }
       formulario = UserFormulario(initial=inicial)
   return render(
       request=request,
       template_name='blog_rodados/formulario_compacto.html',
       context={'formulario': formulario},
   )

def eliminar_compacto(request, id):
   compacto = Compacto.objects.get(id=id)
   if request.method == "POST":
       compacto.delete()
       url_exitosa = reverse('auto_compacto')
       return redirect(url_exitosa)


