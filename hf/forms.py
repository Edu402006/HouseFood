from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #fields = ["nombre", "precio", "descripcion", "nuevo", "marca", "fecha_fabricacion"]
        fields = '__all__'