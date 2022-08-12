import threading
import requests
import socket
import json
import pickle
from random import getrandbits
from ipaddress import IPv4Address
from netaddr import IPNetwork, IPAddress
from datetime import date, datetime
from urllib.request import urlopen

ipsAOmitir = ['0.0.0.0/8', '3.0.0.0/8', '6.0.0.0/7', '10.0.0.0/8', '11.0.0.0/8', '15.0.0.0/7', '21.0.0.0/8', '22.0.0.0/8', '26.0.0.0/8', '28.0.0.0/7', '30.0.0.0/8', '33.0.0.0/8', '55.0.0.0/8', '56.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8', '169.254.0.0/16', '172.16.0.0/14', '192.168.0.0/16', '198.18.0.0/15', '214.0.0.0/7', '224.0.0.0/4']
puertosComunes =  [21, 22, 23, 25, 80, 81, 82, 83, 84, 88, 137, 143, 443, 445, 554, 631, 1080, 1883, 1900, 2000, 2323, 4433, 4443, 4567, 5222, 5683, 7474, 7547, 8000, 8023, 8080, 8081, 8443, 8088, 8883, 8888, 9000, 9090, 9999, 10000, 37777, 49152]

def generarIPsAleatorias ():
    ip = (IPv4Address(getrandbits(32)))
    return ip

def omitirIPs (ip):
    for omitir in ipsAOmitir:
        if (IPAddress(str(ip))) in IPNetwork(omitir):
            return False
    return True

def conectarse (puerto, ip, delay, respuesta):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, puerto))
        for puertos in range(len(puertosComunes)):
            if puerto in puertosComunes:
                print(puerto)
        respuesta[puerto] = 'Puerto escuchando'
    except:
        respuesta[puerto] = ''

def iniciarHilos (hilos):
    for puertos in range(len(puertosComunes)):
        hilos[puertos].start()
        
def joinHilos (hilos):
    for puertos in range(len(puertosComunes)):
        hilos[puertos].join()
 
def escaneo(ip):
    t1 = datetime.now()
    hilos = []
    respuesta = {}
    escuchandoTotal = 0
    puertosActivos = []
    for puerto in puertosComunes:
        t = threading.Thread(target=conectarse, args=(puerto, ip, 2, respuesta))
        hilos.append(t)
    iniciarHilos(hilos)
    joinHilos(hilos)
    for puertos in range(len(puertosComunes)):
        if respuesta[puertosComunes[puertos]] == 'Puerto escuchando':
            puertosActivos.append[puertosComunes[puertos]]
            escuchandoTotal +=1
    return escuchandoTotal, puertosActivos

def lanzarGet(ip, puerto):
    url = 'http://' + ip + ':' + str(puerto)
    print("aaaa")
    try:
        r = requests.get(url, verify=False, timeout=2)
        print(r)
        return r.headers
        r = urlopen(url, timeout=3, verify=False)
        string = r.read().decode('utf-8')
        json_obj = json.loads(string)
        return json_obj
    except Exception as e:
        return 'JSON vacio'
    
def leerDatos (nomArchivo):
    archivo = open(nomArchivo, 'rb')
    try:
        datos = pickle.load(archivo)
    except EOFError:
        datos = set()
    archivo.close()
    return datos

def guardarDatos (nombreArchivo, datos):
    archivo = open(nombreArchivo, 'wb')
    pickle.dump(datos, archivo)
    archivo.close()

def clasificarPuertos (respuesta, ip, puerto):
    hikvision = leerDatos('datosHikvision.dat')
    sonicwall = leerDatos('datosSonicwall.dat')
    netgear = leerDatos('datosNetgear.dat')
    tr069 = leerDatos('datosTR069.dat')
    lighttpd = leerDatos('datosLighttpd.dat')
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
    
def comprobarRespuestaPuertos (ip, puertos):
    for puerto in puertos:
        print(puerto)
        respuesta = lanzarGet(ip, puerto)
        if respuesta != 'JSON vacio':
            print(respuesta)
            clasificarPuertos()

def main ():
    total = 0
    try:
        while True:
            ipsLeidas = leerDatos('ipsLeidas.dat')
            ip = generarIPsAleatorias()
            if ip not in ipsLeidas:
                ipsLeidas.add(ip)
                if omitirIPs(ip):
                    total, puertosActivos = escaneo(ip)
            if total > 0:
                comprobarRespuestaPuertos(ip, puertosActivos)
            ipsLeidas = guardarDatos('ipsLeidas.dat', ipsLeidas)
    except KeyboardInterrupt:
        pass
    
main()