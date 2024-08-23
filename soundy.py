#!/usr/bin/python3
#
# +---------------------------------------------------------------+
# |     ███████╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ ██╗   ██╗     |    
# |     ██╔════╝██╔═══██╗██║   ██║████╗  ██║██╔══██╗╚██╗ ██╔╝     |
# |     ███████╗██║   ██║██║   ██║██╔██╗ ██║██║  ██║ ╚████╔╝      |
# |     ╚════██║██║   ██║██║   ██║██║╚██╗██║██║  ██║  ╚██╔╝       |
# |     ███████║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝   ██║        |
# |     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝    ╚═╝        |
# +-------------------AUTHOR BY: HERO_HZ1999YT--------------------+
#
# -- IMPORTS --
from pyudev import Context, Monitor
from subprocess import Popen
from os import environ, path
from io import open
from sys import exit
from re import sub, match

# -- CONSTANTS --
VERDE = "\033[92m" 
AMARILLO = "\033[93m"
ROJO = "\033[91m"
RESET = "\033[0m"
SOUND_USB_CONNECTED = "/home/" + environ.get('USER') + "/.soundy/sonidos/usb-conectado.mp3"
SOUND_USB_DISCONNECTED = "/home/" + environ.get('USER') + "/.soundy/sonidos/usb-desconectado.mp3"
CONFIG_FILE= "/home/" + environ.get('USER') + "/.soundy/config.azc"
CREDITS_FILE= "/home/" + environ.get('USER') + "/.soundy/creditos.azc"
"""
    OPERACION PARA OBTENER EL VALOR DEL VOLUMEN ES SACANDO EL PORCENTAJE
    MAX_VALUE = 32768
    X_PORCENTAJE = PORCENTAJE CONFIGURADO
    VOLUMEN = (MAX_VALUE*X_PORCENTAJE)/100
"""
SOUND_VOLUME = "32768" # MAX VALUE = 32768

# -- MAIN CLASS --
def soundy():
    creditos()
    context = Context()
    monitor = Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    try:
        # CREAMOS UN CICLO FOR
        for action, device in monitor:
            # VALIDAMOS SI EL ARCHIVO DE CONFIGURACION EXISTE
            existeArchivoConfiguracion()
            # LEEMOS LOS AJUSTES
            leerConfiguracion()
            # VALIDAMOS SI UN DISPOSITIVO FUE AÑADIDO
            if device.action == 'add' and device.get('DEVTYPE') == 'usb_device':
                if path.exists(SOUND_USB_CONNECTED):
                    # MOSTRAMOS QUE UN NUEVO DISPOSITIVO SE A AÑADIDO Y REPRODUCIMOS EL AUDIO
                    print(VERDE + "================================NUEVO DISPOSITIVO AÑADIDO===============================" + RESET)
                    print(VERDE + '{0}: {1}'.format(action, device) + RESET)
                    print(VERDE + "---->>>REPRODUCIENDO SONIDO 7W7<<<----")
                    Popen("mpg123 -f " + SOUND_VOLUME + " " + SOUND_USB_CONNECTED + "&> /dev/null", shell=True)
                    print(VERDE + "========================================================================================" + RESET)              

            # VALIDAMOS SI EL DISPOSITIVO FUE REMOVIDO
            if device.action == 'remove' and device.get('DEVTYPE') == 'usb_device':
                if path.exists(SOUND_USB_DISCONNECTED):
                    # MOSTRAMOS UN MENSAJE POR CONSOLA QUE EL DISPOSITIVO FUE REMOVIDO Y REPRODUCIMOS UN SONIDO
                    print(AMARILLO + "===================================DISPOSITIVO REMOVIDO==================================" + RESET)
                    print(AMARILLO + '{0}: {1}'.format(action, device) + RESET)
                    print(AMARILLO + "---->>>REPRODUCIENDO SONIDO 7W7<<<----")
                    Popen("mpg123 -f " + SOUND_VOLUME + " " + SOUND_USB_DISCONNECTED + "&> /dev/null", shell=True)
                    print(AMARILLO + "========================================================================================" + RESET)
    
    # MOSTRAMOS UN MENSAJE SI EL USUARIO CERRO MANUALMENTE A SOUNDY
    except KeyboardInterrupt:
        print(AMARILLO + "\nEL PROGRAMA FUE CERRADO MANUALMENTE" + RESET)
        exit(1)

# -- FUNCIONS --

"""
    CON ESTA FUNCION VALIDAMOS SI EL ARCHIVO CON LOS CREDITOS SE ENCUENTRA EN LA CARPETA
    DEL PROGRAMA, SI LEES ESTA LINEA RESPETA AL AUTOR ORIGINAL Y OTORGA CREDITOS SI REALIZAS
    ALGUNA MODIFICACION
"""
def creditos():
    if not path.exists(CREDITS_FILE):exit(0)

"""
    FUNCION PARA VALIDAR SI EXISTE EL ARCHIVO DE CONFIGURACION
"""
def existeArchivoConfiguracion():
    if not path.exists(CONFIG_FILE):
        file = open (CONFIG_FILE, "w")
        file.write("#\n" 
                + "# ███████╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ ██╗   ██╗\n"         
                + "# ██╔════╝██╔═══██╗██║   ██║████╗  ██║██╔══██╗╚██╗ ██╔╝\n"         
                + "# ███████╗██║   ██║██║   ██║██╔██╗ ██║██║  ██║ ╚████╔╝ \n"         
                + "# ╚════██║██║   ██║██║   ██║██║╚██╗██║██║  ██║  ╚██╔╝  \n"         
                + "# ███████║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝   ██║   \n"         
                + "# ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝    ╚═╝   \n"         
                + "# --------------AUTHOR BY: HERO_HZ1999YT---------------\n"                
                + "VOLUMEN=100;\n"
            )
        file.close()

"""
    FUNCION PARA LEER NUESTRO ARCHIVO DE CONFIGURACION
"""
def leerConfiguracion():
    global SOUND_VOLUME
    with open (CONFIG_FILE) as archivo:
        for linea in archivo:
            if not linea.startswith("#"):
                # CONFIGURAMOS EL VOLUMEN QUE EL USUARIO ESTABLECIO
                if match("^VOLUMEN=[0-9]+;\\s*$", linea):
                    linea = sub("^VOLUMEN=", "", linea)
                    linea = sub(";\\s*$", "", linea)
                    volumen = int(linea)
                    # VALIDAMOS QUE EL VOLUMEN ESTE ENTR UN RANGO DE 0 A 100
                    if volumen >= 0 and volumen <= 100:
                        SOUND_VOLUME = str(int((32768*int(linea))/100))

# -- EXECUTE MAIN CLASS --
if __name__ == '__main__':
    soundy()