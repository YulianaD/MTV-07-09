
from django.contrib import admin
from django.urls import path
from Cliente.views import facturas, Inicio, recibos, buscar, Busquedacliente, clientes


urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/",clientes),
    path("",Inicio, name="incio"),
    path("Facturas/", facturas),
    path("Recibos/", recibos),
    path("buscar/", buscar, name="buscar"),
    path("Busquedacliente/", Busquedacliente, name="Busquedacliente"),
    

]
