from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Template, Context, loader
# Create your views here.
def familiares(request):
    papa = Familia(nombre = "Manu Pacheco", cedula = 1010154789, nacimiento = "1970-10-14")
    herma = Familia(nombre = "David Pacheco", cedula = 45879632, nacimiento = "1980-7-4")
    mama = Familia(nombre = "Freya Rojas", cedula = 1544799, nacimiento = "1965-5-24")
    papa.save()
    herma.save()
    mama.save()

    # cadena_texto = "Familiar: " + papa.nombre, mama.nombre, herma.nombre + " " + str(papa.cedula) + " " + str(papa.nacimiento) 
    diccionario = {"papa":papa.nombre, "papacedula": papa.cedula, "fechapapa": papa.nacimiento,
                   "herma":herma.nombre, "hermacedula": herma.cedula, "fechaherma": herma.nacimiento,
                   "mama":mama.nombre, "mamacedula": mama.cedula, "fechamama": mama.nacimiento,
                  }

    plantilla = loader.get_template("template_familia.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)