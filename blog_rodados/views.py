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

@login_required
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
   else:  
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

@login_required
def eliminar_compacto(request, id):
   compacto = Compacto.objects.get(id=id)
   if request.method == "POST":
       compacto.delete()
       url_exitosa = reverse('auto_compacto')
       return redirect(url_exitosa)

@login_required   
def crear_compacto(request):
    if request.method == "POST":
        formulario = UserFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            modelo = data["modelo"]
            anio = data["anio"]
            compacto = Compacto(modelo=modelo, anio=anio)
            compacto.save()

            url_exitosa = reverse('auto_compacto')  
            return redirect(url_exitosa)
    else:  
        formulario = UserFormulario()
    http_response = render(
        request=request,
        template_name='blog_rodados/crear_compacto.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_compacto(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        compactos = Compacto.objects.filter(
            Q(modelo__icontains=busqueda) | Q(anio__contains=busqueda)
        )

        contexto = {
            "compactos": compactos,
        }
        http_response = render(
            request=request,
            template_name='blog_rodados/lista_compactos.html',
            context=contexto,
        )
        return http_response


