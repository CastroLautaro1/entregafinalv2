from django.urls import path

from blog_rodados.views import listar_autos


# Son las URLS de la app control_estudios
urlpatterns = [
    path("compactos/", listar_autos, name="auto_compacto"),
]