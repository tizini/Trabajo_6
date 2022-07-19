from django.contrib import admin
from django.urls import path
from App.views import agrega_familiar , lista_familiares

urlpatterns = [
        path('agrega-familiar/<tipo>/<nombre>/<apellido>/<edad>/', agrega_familiar),
        path('lista-familiares/', lista_familiares),
]
