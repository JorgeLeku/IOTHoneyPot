import sys
import json
sys.path.append('../API/')
from apiArchivos import leerDatos, guardarDatos

def clasificarPuertos (respuesta, ip, puerto):
    hikvision = leerDatos('../IoT_Device_Searcher/datos/datosHikvision.dat')
    sonicwall = leerDatos('../IoT_Device_Searcher/datos/datosSonicwall.dat')
    netgear = leerDatos('../IoT_Device_Searcher/datos/datosNetgear.dat')
    tr069 = leerDatos('../IoT_Device_Searcher/datos/datosTR069.dat')
    lighttpd = leerDatos('../IoT_Device_Searcher/datos/datosLighttpd.dat')
    huawei = leerDatos('datosHuawei.dat')
    kangle = leerDatos('datosKangle.dat')
    tplink = leerDatos('datosTpLink.dat')
    webapp = leerDatos('datosWebApp.dat')
    logitech = leerDatos('datosLogitech.dat')
    rh = json.dumps(respuesta.__dict__['_store'])
    print(respuesta)
    if 'Hikvision'.lower() in rh.lower() or 'DVRDVS'.lower() in rh.lower():
        hikvision.add(ip + ":" + str(puerto))
    elif 'SonicWALL'.lower() in rh.lower():
        sonicwall.add(ip + ":" + str(puerto))
    elif 'NETGEAR'.lower() in rh.lower():
        netgear.add(ip + ":" + str(puerto))
    elif 'TR069'.lower() in rh.lower() or 'gSOAP'.lower() in rh.lower() or 'TR-069'.lower() in rh.lower():
        tr069.add(ip + ":" + str(puerto))
    elif 'lighttpd'.lower() in rh.lower():
        lighttpd.add(ip + ":" + str(puerto))
    elif 'HuaweiHomeGateway'.lower() in rh.lower():
        huawei.add(ip + ":" + str(puerto))
    elif 'kangle'.lower() in rh.lower():
        kangle.add(ip + ":" + str(puerto))
    elif 'TP-LINK'.lower() in rh.lower():
        tplink.add(ip + ":" + str(puerto))
    elif 'Logitech'.lower() in rh.lower():
        logitech.add(ip + ":" + str(puerto))
    elif 'App-webs'.lower() in rh.lower():
        webapp.add(ip + ":" + str(puerto))
    hikvision = guardarDatos('datosHikvision.dat')
    sonicwall = guardarDatos('datosSonicwall.dat')
    netgear = guardarDatos('datosNetgear.dat')
    tr069 = guardarDatos('datosTR069.dat')
    lighttpd = guardarDatos('datosLighttpd.dat')
    huawei = guardarDatos('datosHuawei.dat')
    kangle = guardarDatos('datosKangle.dat')
    tplink = guardarDatos('datosTpLink.dat')
    webapp = guardarDatos('datosWebApp.dat')
    logitech = guardarDatos('datosLogitech.dat')
    