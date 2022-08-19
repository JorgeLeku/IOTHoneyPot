import threading
import requests
import socket
import json
import sys
sys.path.append('../API/')
from random import getrandbits
from ipaddress import IPv4Address
from netaddr import IPNetwork, IPAddress
from datetime import date, datetime
from urllib.request import urlopen
from apiArchivos import leerDatos, guardarDatos
from clasificarRespuestas import clasificarPuertos


ipsAOmitir = ['0.0.0.0/8', '3.0.0.0/8', '6.0.0.0/7', '10.0.0.0/8', '11.0.0.0/8', '15.0.0.0/7', '21.0.0.0/8', '22.0.0.0/8', '26.0.0.0/8', '28.0.0.0/7', '30.0.0.0/8', '33.0.0.0/8', '55.0.0.0/8', '56.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8', '169.254.0.0/16', '172.16.0.0/14', '192.168.0.0/16', '198.18.0.0/15', '214.0.0.0/7', '224.0.0.0/4']
puertosComunes =  [21, 22, 23, 25, 80, 81, 82, 83, 84, 88, 137, 143, 443, 445, 554, 631, 1080, 1883, 1900, 2000, 2323, 4433, 4443, 4567, 5222, 5683, 7474, 7547, 8000, 8023, 8080, 8081, 8443, 8088, 8883, 8888, 9000, 9090, 9999, 10000, 37777, 49152]
headers = {'User-Agent': None, 'Host': None, 'Accept-Encoding': None, 'Accept': None, 'Connection': None}

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
        TCPsock.connect((str(ip), puerto))
        print("Puerto responde ")
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
            print(puertosComunes[puertos])
            puertosActivos.append([puertosComunes[puertos]])
            print(puertosActivos)
            escuchandoTotal +=1
    return escuchandoTotal, puertosActivos

def lanzarGet(ip, puerto):
    url = 'http://' + str (ip) + ':' + str(puerto)
    print("aaaa")
    try:
        r = requests.get(url, verify=False, timeout=2)
        print(r)
        return r.headers
    except Exception as e:
        return 'JSON vacio'

def comprobarRespuestaPuertos (ip, puertos):
    print("Comprobar respuesta Puertos")
    for puerto in puertos:
        print("Comprobar respuesta Puertos " + str (puerto[0]))
        print(puerto)
        respuesta = lanzarGet(ip, str (puerto[0]))
        if respuesta != 'JSON vacio':
            print(respuesta)
            clasificarPuertos(respuesta, str(ip), str (puerto[0]))
            enviarGet(ip, puerto)

def enviarGet (ip, puerto):
    datosRespuestasPorDefecto = leerDatos('../IoT_Device_Searcher/datos/datosRespuestasPorDefecto.dat')
    try:
        resp = requests.get('http://' + str(ip) + ":" + str(puerto[0]) + '/login.cgi', headers=headers, verify=False, timeout=2)
        print(str(resp))
        datosRespuestasPorDefecto.add(resp)
        guardarDatos('../IoT_Device_Searcher/datos/datosRespuestasPorDefecto.dat', datosRespuestasPorDefecto)
    except:
        print('Error al pedir login a: ' + str(ip) + ':' + str(puerto))

def main ():
    total = 0
    try:
        while True:
            ipsLeidas = leerDatos('../IoT_Device_Searcher/datos/ipsLeidas.dat')
            ip = generarIPsAleatorias()
            if ip not in ipsLeidas:
                ipsLeidas.add(ip)
                if omitirIPs(ip):
                    total, puertosActivos = escaneo(ip)
            if total > 0:
                comprobarRespuestaPuertos(ip, puertosActivos)
            guardarDatos('../IoT_Device_Searcher/datos/ipsLeidas.dat', ipsLeidas)
    except KeyboardInterrupt:
        pass
    
main()