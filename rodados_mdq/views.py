from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludamiento(request):
    saludo = "Hola usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html