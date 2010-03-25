# -*- coding: utf-8 -*-

import urllib
import os
info="-*- Información publicada automáticamente mediante el script 'crearnota' de canaima:\n\n"
info+="-\n"
info+="----- Dispositivos conectados por PCI:\n"
info+="-\n"
info+=os.popen("lspci").read()
info+="-\n"
info+="----- Dispositivos conectados por puerto USB:\n\n"
info+="-\n"
info+=os.popen("lsusb").read()
info+="-\n"
info+="----- Información sobre su tarjeta gráfica:\n\n"
info+="-\n"
info+=os.popen("glxinfo").read()



params = urllib.urlencode({'codigo_form': info, 'titulo_form': "Desde consola",'nombre_form': "nombre"})
f = urllib.urlopen("http://172.16.130.67:8000/enviar_consola", params)
print f.read()

