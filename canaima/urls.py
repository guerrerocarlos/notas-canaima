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

    (r'^bienvenido/', bienvenido),
    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
