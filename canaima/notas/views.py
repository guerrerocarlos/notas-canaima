# Create your views here.
from django.shortcuts import render_to_response
from canaima.notas.models import *
from django.http import HttpResponse



def bienvenido(request):
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    return render_to_response('1.html',{'notas_recientes': notas_recientes})

def enviar(request,url):
    errors = []
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    if 'codigo_form' in request.POST:
        codigo_form = request.POST['codigo_form']
        titulo_form = request.POST['titulo_form']
        autor_form = request.POST['nombre_form']
	a1=Autor(name=autor_form)
	a1.save()
        p1 = Nota(nota=codigo_form,titulo=titulo_form,autor=a1)
	p1.save()
        return render_to_response('1.html',{'exito': True,'notas_recientes': notas_recientes})
    return render_to_response('1.html',{'errors': errors})
    

def enviar2(request):
    errors = []
    if 'codigo_form' in request.POST:
       titulo_form = request.POST['titulo_form']
       autor_form = request.POST['nombre_form']
       codigo_form = request.POST['codigo_form']
       return HttpResponse(codigo_form+titulo_form+autor_form)
    return HttpResponse("Error")
 

