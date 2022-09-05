from django.shortcuts import render
from models import *
from django.template import context, Template, loader
from django.http import HttpResponse

# Create your views here.



def cliente(request):
  cliente1= clientes(nombre="",número=1000, fecha_de_emisión="25-08-2022")
  cliente2= clientes(nombre="",número=1001, fecha_de_emisión="01-07-2022")
  cliente3= clientes(nombre="",número=1002, fecha_de_emisión="10-01-2022")

  cliente1.save()
  cliente2.save()
  cliente3.save()
  clientes={"nombre":cliente1.nombre,"número":cliente1.número,"fecha_de_emisión":cliente1.fecha_de_emisión,"nombre":cliente2.nombre,"número":cliente2.número,"fecha_de_emisión":cliente2.fecha_de_emisión,"nombre":cliente3.nombre,"número":cliente3.número,"fecha_de_emisión":cliente3.fecha_de_emisión,}
  plantillas=loader.get_template("template1.html")
  clientes=plantillas.render(clientes)
  
  return HttpResponse("clientes")
