from django.urls import path

from blog_rodados.views import listar_compactos


# Son las URLS de la app control_estudios
urlpatterns = [
    path("compactos/", listar_compactos, name="auto_compacto"),   
]