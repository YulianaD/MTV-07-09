from django.contrib import admin
from Clientes.Cliente.views import cliente
from models import *
# Register your models here.


admin.site.register(facturas)
admin.site.register(recibo)
admin.site.register(retenciones)
admin.site.register(clientes)
