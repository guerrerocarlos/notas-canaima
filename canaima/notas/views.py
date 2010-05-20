# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from canaima.notas.models import *
from django.http import HttpResponse
from canaima.notas.forms import formulario_principal

	


def buscar(request):

    fp=formulario_principal()
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    if 'q' in request.GET:
        busqueda = request.GET['q']
	resultados = Nota.objects.filter(nota__contains=busqueda)
	resultados3 = Nota.objects.filter(titulo__contains=busqueda)
	resultados2 = Nota.objects.filter(autor__name__contains=busqueda)
        return render_to_response('1.html',{'todas': resultados,'todas2': resultados2,'todas3':resultados3,'notas_recientes':notas_recientes,'busqueda':True,'formulario_principal':fp})


def bienvenido(request):
    fp=formulario_principal()
    if "mostrar" in request.COOKIES:
	salida = request.COOKIES["mostrar"]
	if salida == "no":
		mostrar_ayuda=False
	else:
		mostrar_ayuda=True
    else:
	mostrar_ayuda=True
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    return render_to_response('1.html',{'notas_recientes': notas_recientes,'nueva':True, 'mayuda':mostrar_ayuda,'formulario_principal':fp})


def enviar_consola(request):
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
        return HttpResponse('La información sobre su equipo ha sido publicada en: http://notas.canaima.softwarelibre.gob.ve/'+str(p1.id))
    return HttpResponse('Se ha producido un error')


def enviar(request):


    form = formulario_principal(request.POST)
    fp=formulario_principal()
    if (form.is_valid()):

	    errors = []
	    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
	    fp=formulario_principal()
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
	    	return render_to_response('1.html',{'exito':True,'id':p1.id,'notas_recientes':notas_recientes,'formulario_principal':fp})
	    return render_to_response('1.html',{'errors': errors,'exito':True,'notas_recientes':notas_recientes,'formulario_principal':fp})
    else:

	notas_recientes = Nota.objects.order_by('-fecha')[0:7]
	errors=formulario_principal(form)
	return render_to_response('1.html',{'errors': "Error en la informacion del formulario",'exito':False,'notas_recientes':notas_recientes,'formulario_principal':fp})




def ver(request,num ):
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    fp=formulario_principal()
    aver=Nota.objects.get(id=num)
    lineas=aver.nota.split("\n")
    return render_to_response('1.html',{'ver': aver,'ver2':lineas,'nim':num,'notas_recientes': notas_recientes,'formulario_principal':fp})

def mostrar_archivo(request):
    todas_notas = Nota.objects.order_by('-fecha')
    fp=formulario_principal()
    return render_to_response('1.html',{'todas': todas_notas,'formulario_principal':fp})

def mostrar_ayuda(request):

    fp=formulario_principal()
    notas_recientes = Nota.objects.order_by('-fecha')[0:7]
    return render_to_response('1.html',{'ayuda': True,'notas_recientes':notas_recientes,'formulario_principal':fp})



def enviar2(request):
    errors = []
    fp=formulario_principal()
    if 'codigo_form' in request.POST:
       titulo_form = request.POST['titulo_form']
       autor_form = request.POST['nombre_form']
       codigo_form = request.POST['codigo_form']
       return HttpResponse(codigo_form+titulo_form+autor_form)
    return HttpResponse("Error")
 

