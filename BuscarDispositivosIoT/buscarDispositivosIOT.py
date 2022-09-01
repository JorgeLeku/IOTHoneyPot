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
from apiArchivos import leerDatos, guardarDatos, leerDatosTxt
from clasificarRespuestas import clasificarPuertos


headers = {'User-Agent': None, 'Host': None, 'Accept-Encoding': None, 'Accept': None, 'Connection': None}
puertosComunes = []
# Genera una IP aleatoria
def generarIPsAleatorias ():
    ip = (IPv4Address(getrandbits(32)))
    return ip

# Recoge los puertos comunes usados en dispositivos IoT
def leerPuertos():
    global puertosComunes
    puertosComunes = leerDatosTxt("../IoT_Device_Searcher/datos/PuertosABuscar.txt")
    
# Omite las ips introducidas por defecto, para de esta forma evitar analizar IPs no deseadas
def omitirIPs (ip):
    ipsAOmitir = leerDatosTxt("../IoT_Device_Searcher/datos/IPsAIgnorar.txt")
    for omitir in ipsAOmitir:
        if (IPAddress(str(ip))) in IPNetwork(omitir):
            return False
    return True

# Se conecta a los diferentes puertos de una IP en busca de un puerto abierto
def conectarse (puerto, ip, delay, respuesta):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((str(ip), puerto))
        print("Puerto responde ")
        if puerto in puertosComunes:
            print(puerto)
        respuesta[puerto] = 'Puerto escuchando'
    except:
        respuesta[puerto] = ''

# Genera tantos hilos como puertos para realizar una busqueda en cada hilo y así ser mas eficiente
def iniciarHilos (hilos):
    for puertos in range(len(puertosComunes)):
        hilos[puertos].start()
        
def joinHilos (hilos):
    for puertos in range(len(puertosComunes)):
        hilos[puertos].join()
 
# Realiza un escaneo de la IP en busca de puertos abiertos
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

# En el caso de que se encuentre un puerto abierto, lanza un get para recoger respuestas
def lanzarGet(ip, puerto):
    url = 'http://' + str (ip) + ':' + str(puerto)
    print("aaaa")
    try:
        r = requests.get(url, verify=False, timeout=2)
        print(r)
        return r.headers
    except Exception as e:
        return 'JSON vacio'

# Comprueba que la respuesta obtenida en lanzarGet sea valida y si es asi la envia a clasificarRespuestas para clasificarla y guardarla
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

# Lanza un get para obtener las respuestas que devolveremos nosotros en el honeypot
def enviarGet (ip, puerto):
    datosRespuestasPorDefecto = leerDatos('../IoT_Device_Searcher/datos/datosRespuestasPorDefecto.dat')
    try:
        resp = requests.get('http://' + str(ip) + ":" + str(puerto[0]) + '/login.cgi', headers=headers, verify=False, timeout=2)
        print(str(resp))
        datosRespuestasPorDefecto.add(resp)
        guardarDatos('../IoT_Device_Searcher/datos/datosRespuestasPorDefecto.dat', datosRespuestasPorDefecto)
    except:
        print('Error al pedir login a: ' + str(ip) + ':' + str(puerto))

# Metodo main
def main ():
    total = 0
    leerPuertos()
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