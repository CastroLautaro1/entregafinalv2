from django.contrib import admin

# Register your models here.

from blog_rodados.models import Articulo, Compacto, SUV, Sedan, PickUp

admin.site.register(Articulo)
admin.site.register(Compacto)
admin.site.register(SUV)
admin.site.register(Sedan)
admin.site.register(PickUp)


