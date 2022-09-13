from django.db import models

# Create your models here.

class recibo(models.Model):
    nombre_de_cliente= models.CharField(max_length=50)
    número= models.IntegerField()
    fecha_de_emisión = models.DateField()

class facturas(models.Model):
    nombre_de_cliente= models.CharField(max_length=50)
    número= models.IntegerField()
    fecha_de_emisión = models.DateField()

class retenciones(models.Model):
    nombre_de_cliente= models.CharField(max_length=50)
    número= models.IntegerField()
    fecha_de_emisión = models.DateField()

class clientes(models.Model):
    nombre_de_cliente= models.CharField(max_length=50)
    número= models.IntegerField()
    fecha_de_alta = models.DateField()

   