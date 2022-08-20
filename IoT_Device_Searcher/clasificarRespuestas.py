import sys
import json
sys.path.append('../API/')
from apiArchivos import leerDatos, guardarDatos

# Organiza las respuestas en diferentes archivos
def clasificarPuertos (respuesta, ip, puerto):
    guardarEn = ''
    rh = json.dumps(respuesta.__dict__['_store'])      
    if 'kangle'.lower() in rh.lower():
        guardarEn = 'datosKangleResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'SonicWALL'.lower() in rh.lower():
        guardarEn = 'datosSonicwallResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'NETGEAR'.lower() in rh.lower():
        guardarEn = 'datosNetgearResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'Hikvision'.lower() in rh.lower() or 'DVRDVS'.lower() in rh.lower():
        guardarEn = 'datosHikvisionResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'lighttpd'.lower() in rh.lower():
        guardarEn = 'datosLighttpdResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'HuaweiHomeGateway'.lower() in rh.lower():
        guardarEn = 'datosHuaweiResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'TP-LINK'.lower() in rh.lower():
        guardarEn = 'datosTpLinkResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'Logitech'.lower() in rh.lower():
        guardarEn = 'datosLogitechResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'App-webs'.lower() in rh.lower():
        guardarEn = 'datosWebAppResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'TR069'.lower() in rh.lower() or 'TR-069'.lower() in rh.lower():
        guardarEn = 'datosTR069Resp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    else:
        guardarEn = 'datosOtrosResp'
        abrir(guardarEn)
        guardarEn.add(str(ip) + ":" + str(puerto) + str(respuesta))
    guardarDatos(guardarEn, guardarEn)
    
# Abre el archivo en concreto
def abrir(archivo):
    archivo = leerDatos('../IoT_Device_Searcher/datos/RespuestasCompletas/' + archivo + '.dat')
    return archivo

# Guarda los datos en el archivo
def guardar(dato, archivo):
    guardarDatos('../IoT_Device_Searcher/datos/RespuestasCompletas/' + dato + '.dat', archivo)
