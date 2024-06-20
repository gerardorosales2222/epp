from django.shortcuts import render
from app1.models import *

def index(request):
    return render(request,'index.html')

def mas_info(request):
    return render(request,'mas_info.html')

def terminos_uso(request):
    return render(request,'terminos_uso.html')

def politica_privacidad(request):
    return render(request,'politica_privacidad.html')

def soporte_tecnico(request):
    return render(request,'soporte.html')

def obreros_vista(request):
    o = obreros.objects.all()
    lista={'obreros':o}
    return render(request, 'obreros.html',lista)

def epps(request):
    e = epp.objects.all()
    lista={'epps':e}
    return render(request, 'epps.html',lista)

def ordenes_retiro(request):
    o = orden_de_retiro.objects.all()
    lista={'or':o}
    return render(request, 'ordenes_retiro.html',lista)