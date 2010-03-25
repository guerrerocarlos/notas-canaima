# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from django.http import Http404, HttpResponseRedirect

from canaima.notas.models import *
from django.http import HttpResponse






def bienvenido(request):
    if "mostrar" in request.COOKIES:
	salida = request.COOKIES["mostrar"]
	if salida == "no":
		mostrar_ayuda=False
	else:
		mostrar_ayuda=True
    else:
	mostrar_ayuda=True
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    return render_to_response('1.html',{'notas_recientes': notas_recientes,'nueva':True, 'mayuda':mostrar_ayuda})

def enviar(request):
    errors = []
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    if 'codigo_form' in request.POST:
        codigo_form = request.POST['codigo_form']
        titulo_form = request.POST['titulo_form']
        autor_form = request.POST['nombre_form']
	if ( autor_form!="") :
		a1=Autor(name=autor_form)
	else :
		a1=Autor(name="Anónimo")
	a1.save()

	if ( titulo_form==""):
        	p1 = Nota(nota=codigo_form,titulo="Sin Título",autor=a1)
	else:
        	p1 = Nota(nota=codigo_form,titulo=titulo_form,autor=a1)
	p1.save()
    	return render_to_response('1.html',{'exito':True,'id':p1.id,'notas_recientes':notas_recientes})
    return render_to_response('1.html',{'errors': errors,'exito':True,'notas_recientes':notas_recientes})
    

def ver(request,num ):
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    aver=Nota.objects.get(id=num)
    lineas=aver.nota.split("\n")
    return render_to_response('1.html',{'ver': aver,'ver2':lineas,'nim':num,'notas_recientes': notas_recientes})

def mostrar_archivo(request):
    todas_notas = Nota.objects.order_by('-fecha')
    return render_to_response('1.html',{'todas': todas_notas})

def mostrar_ayuda(request):

    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    return render_to_response('1.html',{'ayuda': True,'notas_recientes':notas_recientes})



def enviar2(request):
    errors = []
    if 'codigo_form' in request.POST:
       titulo_form = request.POST['titulo_form']
       autor_form = request.POST['nombre_form']
       codigo_form = request.POST['codigo_form']
       return HttpResponse(codigo_form+titulo_form+autor_form)
    return HttpResponse("Error")
 

