from django.test import TestCase

# Create your tests here.

from blog_rodados.models import Compacto


class CompactoTests(TestCase):
    """En esta clase van todas las pruebas del modelo Compacto."""

    def test_creacion_compacto(self):
        # caso uso esperado
        compacto = Compacto(modelo="Titulo", anio=1000)
        compacto.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Compacto.objects.count(), 1)
        self.assertEqual(compacto.modelo, "Titulo")
        self.assertEqual(compacto.anio, 1000)

    def test_curso_str(self):
        compacto = Compacto(modelo="POLO COMFORTLINE", anio=2021)
        compacto.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(compacto.__str__(), "POLO COMFORTLINE (2021)")