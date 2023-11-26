from django.urls import path

from blog_rodados.views import listar_compactos, listar_sedanes, listar_suv, listar_pickup, modelos


# Son las URLS de la app control_estudios
urlpatterns = [
    path("compacto/", listar_compactos, name="auto_compacto"), 
    path("sedan/", listar_sedanes, name="auto_sedan"), 
    path("suv/", listar_suv, name="auto_suv"), 
    path("pickup/", listar_pickup, name="auto_pickup"),
    path("modelos/", modelos, name="lista_modelos"),  
]