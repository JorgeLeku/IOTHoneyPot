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
    huawei = leerDatos('../IoT_Device_Searcher/datos/datosHuawei.dat')
    kangle = leerDatos('../IoT_Device_Searcher/datos/datosKangle.dat')
    tplink = leerDatos('../IoT_Device_Searcher/datos/datosTpLink.dat')
    webapp = leerDatos('../IoT_Device_Searcher/datos/datosWebApp.dat')
    logitech = leerDatos('../IoT_Device_Searcher/datos/datosLogitech.dat')
    otros = leerDatos('../IoT_Device_Searcher/datos/datosOtros.dat')
    imprimir = leerDatos('../IoT_Device_Searcher/datos/response_from_iot.dat')

    hikvisionResp = leerDatos('../IoT_Device_Searcher/datos/datosHikvisionResp.dat')
    sonicwallResp = leerDatos('../IoT_Device_Searcher/datos/datosSonicwallResp.dat')
    netgearResp = leerDatos('../IoT_Device_Searcher/datos/datosNetgearResp.dat')
    tr069Resp = leerDatos('../IoT_Device_Searcher/datos/datosTR069Resp.dat')
    lighttpdResp = leerDatos('../IoT_Device_Searcher/datos/datosLighttpdResp.dat')
    huaweiResp = leerDatos('../IoT_Device_Searcher/datos/datosHuaweiResp.dat')
    kangleResp = leerDatos('../IoT_Device_Searcher/datos/datosKangleResp.dat')
    tplinkResp = leerDatos('../IoT_Device_Searcher/datos/datosTpLinkResp.dat')
    webappResp = leerDatos('../IoT_Device_Searcher/datos/datosWebAppResp.dat')
    logitechResp = leerDatos('../IoT_Device_Searcher/datos/datosLogitechResp.dat')
    otrosResp = leerDatos('../IoT_Device_Searcher/datos/datosOtrosResp.dat')

    
    rh = json.dumps(respuesta.__dict__['_store'])
    print("sadsdadsda")
    print(imprimir)
    print("adadwdwada")
    print(ip + ":" + str(puerto))
    if 'Hikvision'.lower() in rh.lower() or 'DVRDVS'.lower() in rh.lower():
        hikvision.add(str(ip) + ":" + str(puerto))
    elif 'SonicWALL'.lower() in rh.lower():
        sonicwall.add(str(ip) + ":" + str(puerto))
    elif 'NETGEAR'.lower() in rh.lower():
        netgear.add(str(ip) + ":" + str(puerto))
    elif 'TR069'.lower() in rh.lower() or 'gSOAP'.lower() in rh.lower() or 'TR-069'.lower() in rh.lower():
        tr069.add(str(ip) + ":" + str(puerto))
    elif 'lighttpd'.lower() in rh.lower():
        lighttpd.add(str(ip) + ":" + str(puerto))
    elif 'HuaweiHomeGateway'.lower() in rh.lower():
        huawei.add(str(ip) + ":" + str(puerto))
    elif 'kangle'.lower() in rh.lower():
        kangle.add(str(ip) + ":" + str(puerto))
    elif 'TP-LINK'.lower() in rh.lower():
        tplink.add(str(ip) + ":" + str(puerto))
    elif 'Logitech'.lower() in rh.lower():
        logitech.add(str(ip) + ":" + str(puerto))
    elif 'App-webs'.lower() in rh.lower():
        webapp.add(str(ip) + ":" + str(puerto))
    else:
        otros.add(str(ip) + ":" + str(puerto))
        
    if 'Hikvision'.lower() in rh.lower() or 'DVRDVS'.lower() in rh.lower():
        hikvisionResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'SonicWALL'.lower() in rh.lower():
        sonicwallResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'NETGEAR'.lower() in rh.lower():
        netgearResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'TR069'.lower() in rh.lower() or 'gSOAP'.lower() in rh.lower() or 'TR-069'.lower() in rh.lower():
        tr069Resp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'lighttpd'.lower() in rh.lower():
        lighttpdResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'HuaweiHomeGateway'.lower() in rh.lower():
        huaweiResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'kangle'.lower() in rh.lower():
        kangleResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'TP-LINK'.lower() in rh.lower():
        tplinkResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'Logitech'.lower() in rh.lower():
        logitechResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    elif 'App-webs'.lower() in rh.lower():
        webappResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
    else:
        otrosResp.add(str(ip) + ":" + str(puerto) + str(respuesta))
        
    guardarDatos('../IoT_Device_Searcher/datos/datosHikvision.dat', hikvision)
    guardarDatos('../IoT_Device_Searcher/datos/datosSonicwall.dat', sonicwall)
    guardarDatos('../IoT_Device_Searcher/datos/datosNetgear.dat', netgear)
    guardarDatos('../IoT_Device_Searcher/datos/datosTR069.dat', tr069)
    guardarDatos('../IoT_Device_Searcher/datos/datosLighttpd.dat', lighttpd)
    guardarDatos('../IoT_Device_Searcher/datos/datosHuawei.dat', huawei)
    guardarDatos('../IoT_Device_Searcher/datos/datosKangle.dat', kangle)
    guardarDatos('../IoT_Device_Searcher/datos/datosTpLink.dat', tplink)
    guardarDatos('../IoT_Device_Searcher/datos/datosWebApp.dat', webapp)
    guardarDatos('../IoT_Device_Searcher/datos/datosLogitech.dat', logitech)
    guardarDatos('../IoT_Device_Searcher/datos/datosOtros.dat', otros)
    
    guardarDatos('../IoT_Device_Searcher/datos/datosHikvisionResp.dat', hikvisionResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosSonicwallResp.dat', sonicwallResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosNetgearResp.dat', netgearResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosTR069Resp.dat', tr069Resp)
    guardarDatos('../IoT_Device_Searcher/datos/datosLighttpdResp.dat', lighttpdResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosHuaweiResp.dat', huaweiResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosKangleResp.dat', kangleResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosTpLinkResp.dat', tplinkResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosWebAppResp.dat', webappResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosLogitechResp.dat', logitechResp)
    guardarDatos('../IoT_Device_Searcher/datos/datosOtrosResp.dat', otrosResp)