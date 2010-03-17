# Create your views here.
from django.shortcuts import render_to_response
from canaima.notas.models import *

def bienvenido(request):
    notas_recientes = Nota.objects.order_by('fecha')
    return render_to_response('1.html',{'notas_recientes': notas_recientes})

