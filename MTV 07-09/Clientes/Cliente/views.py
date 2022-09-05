from django.shortcuts import render
from models import *
from django.template import context, Template, loader
from django.http import HttpResponse
from forms import ClientForm

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

def Inicio(request):
    return render (request, "Clientes\Plantilla\Clientes.html")

def clientes(request):
  return render (request, "Clientes\Plantilla\Clientes.html")


def facturas(request):
  return render (request, "Clientes\Plantilla\Facturas.html")  

def recibos(request):
  return render (request, "Clientes\Plantilla\Recibos.html")  


def Clientes(request):

    if request.method=="POST":
        form= ClientForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            número= info["número"]
            email= info["email"]
            cliente= Clientes(nombre=nombre, número=número, email=email)
            cliente.save()
            return render (request, "Clientes\Plantilla\Inicio.html", {"mensaje":"Cliente creado"})
    else:
        form= ClientForm()
    return render(request, "Clientes\Plantilla\Clientes.html", {"formulario":form})

##################################################################################################
def Busquedacliente(request):
    return render(request, "Clientes/Busquedacliente.html")

def buscar(request):
    if request.GET["clientes"]:

      número=request.GET["número"]
       
      Clientes=Clientes.objects.filter(número=número)
      return render(request, "Clientes/ResultadosBusqueda.html", {"Clientes":Clientes})
    else:
      return render(request, "Clientes/Busquedacliente.html", {"mensaje":"Por favor, ingrese un cliente válido"})
    
    return HttpResponse(respuesta)



