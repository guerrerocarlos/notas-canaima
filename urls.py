from django.conf.urls.defaults import *
from django.contrib import admin
from canaima.notas.views import *
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^canaima/', include('canaima.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^1_archivos/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/guerrerocarlos/www.tecnoguardian.com/data/1_archivos'}),
    (r'^data/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/guerrerocarlos/www.tecnoguardian.com/data/'}),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
#    (r'^ver/(?P<num>.*)$', ver),
    (r'([0-9^/]+)', ver),
    (r'^enviar2', enviar2),
    (r'^buscar', buscar),

    (r'^enviar_consola', enviar_consola),
    (r'^enviar', enviar),
    (r'^archivo', mostrar_archivo),
    (r'^ayuda', mostrar_ayuda),
    (r'^', bienvenido),
)
