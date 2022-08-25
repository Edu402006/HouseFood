from django.urls import path
from .views import home, bodega, caja, finanza, mesas

urlpatterns = [
    path('', home, name="home"),
    path('bodega/', bodega, name="bodega"),
    path('caja/', caja, name="caja"),
    path('finanza/', finanza, name="finanza"),
    path('mesas', mesas, name="mesas"),
]