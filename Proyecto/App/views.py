from django.shortcuts import render
from App.models import Familia
from django.http import HttpResponse

# Create your views here.

def agrega_familiar(self, tipo, nombre, apellido, edad):

    familiar = Familia(tipo=tipo, nombre=nombre, apellido=apellido, edad=edad)
    familiar.save()

    return HttpResponse(f"""
            <p>El familiar tipo: {familiar.tipo} con nombre: {familiar.nombre}, apellido{familiar.apellido} y edad: {familiar.edad} se agrego a la DB</p>
    """)

def lista_familiares(self):

    lista_f = Familia.objects.all()

    return render(self, "familia.html", {"lista_familiares": lista_f})