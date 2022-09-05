from django.apps import AppConfig

from Clientes.Cliente.models import facturas


class ClienteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Cliente"



