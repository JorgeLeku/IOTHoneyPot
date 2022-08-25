import socket
import sys
import random

sys.path.append('../API/')
from apiArchivos import leerDatos, guardarDatos
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

respuestas = leerDatos('../IoT_Device_Searcher/datos/datosRespuestasPorDefecto.dat')

def inicializarDatos():
    puerto = int(input("Introducir puerto: "))
    ipSrv = str(input("Introducir IP: "))
    ip = (ipSrv, puerto)
    print('inicializando servidor en la ip {} y puerto {}'.format(*ip))
    sock.bind(ip)
    sock.listen(1)
    return(ip)
    
def responderAConexion(connection, client_address, ip):
    while True:
        dato = connection.recv(16)
        dt =+ str(dato)
        print('dato {!r}'.format(dato))
        if dato:
            print('Respondiendo al cliente')
            dir, response = random.choice(list(respuestas.items()))
            connection.sendall(response.content)
        else:
            print('sin datos del cliente', client_address)
            break
    return(dt, dir)

def main():
    ip = inicializarDatos()
    try:
        while True:
            datos = leerDatos('../IoT_HoneyPot/DatosObtenidos/puerto' + str(ip[1]) + '.dat')
            ips = leerDatos('../IoT_HoneyPot/IPsConectadas/puerto' + str(ip[1]) + '.dat')
            print('A la espera')
            try:
                conn, dirCli = sock.accept()
            except KeyboardInterrupt:
                print("Cancelado. Terminando ejecución")

            print('Conexion recibida de', dirCli)
            dt, dir = responderAConexion(conn, dirCli, ip, datos)
            ips.add(dir)
            datos.add(dt)
            guardarDatos('../IoT_HoneyPot/IPsConectadas/puerto' + str(ip) + '.dat', ips)
            guardarDatos('../IoT_HoneyPot/DatosObtenidos/puerto' + str(ip) + '.dat', dt)
    except KeyboardInterrupt:
        print("Cancelado. Terminando ejecución")

main()