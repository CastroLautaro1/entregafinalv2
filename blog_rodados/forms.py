from django import forms

class UserFormulario(forms.Form):
    modelo = forms.CharField(required=True, max_length=64)
    anio = forms.IntegerField(required=True, max_value=80000)