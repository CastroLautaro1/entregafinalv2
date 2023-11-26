from django import forms

class AutoFormulario(forms.Form):
    modelo = forms.CharField(required=True, max_length=64)
    año = forms.IntegerField(required=True, max_value=80000)