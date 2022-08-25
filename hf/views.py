from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def home(request):
    return render(request, 'hf/home.html')

def bodega(request):
    productosListados = Producto.objects.all()
    return render(request, 'hf/bodega.html', {"productos": productosListados})


def caja(request):
    return render(request, 'hf/caja.html')

def finanza(request):
    return render(request, 'hf/finanza.html')

def mesas(request):
    return render(request, 'hf/mesas.html')