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
info+="-\n"
info+="----- Información sobre su memoria RAM (en MB):\n\n"
info+="-\n"
info+=os.popen("free -m").read()
info+="-\n"
info+="----- Información sobre su espacio libre :\n\n"
info+="-\n"
info+=os.popen("df -h").read()
info+="-\n"
info+="----- Información sobre sus discos duros :\n\n"
info+="-\n"
info+=os.popen("fdisk -l").read()


params = urllib.urlencode({'codigo_form': info, 'titulo_form': "Desde consola",'nombre_form': "nombre"})
f = urllib.urlopen("http://172.16.130.67:8000/enviar_consola", params)
print f.read()

