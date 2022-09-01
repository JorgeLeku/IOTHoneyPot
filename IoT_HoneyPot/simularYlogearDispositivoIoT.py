import socket
import sys
import random

sys.path.append('../API/')
from apiArchivos import leerDatos, guardarDatos
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

respuestas = leerDatos('../BuscarDispositivosIoT/datos/datosRespuestasPorDefecto.dat')

def inicializarDatos():
    puerto = sys.argv[2]
    ipSrv = sys.argv[1]
    ip = (ipSrv, int(puerto))
    print('ip ' + ipSrv + ' puerto ' + puerto)
    print('inicializando servidor en la ip {} y puerto {}'.format(*ip))
    sock.bind(ip)
    sock.listen(1)
    return(ip)

def responderAConexion(connection, dirCli, ip):
    dt = ''
    while True:
        dato = connection.recv(16)
        print(dato)
        dt = dt+ str(dato)

        print('dato {!r}'.format(dato))
        if dato:
            print('Respondiendo al cliente')

            dir, response = random.choice(list(respuestas.items()))
            
            connection.sendall(response.content)
        else:
            print('sin datos del cliente', dirCli)
            break
    return(dt, dir)

def main():
    ip = inicializarDatos()
    try:
        while True:
            datos = leerDatos('../IoT_HoneyPot/DatosObtenidos/puerto' + str(ip[1]) + '.dat')
            ips = leerDatos('../IoT_HoneyPot/IPsConectadas/puerto' + str(ip[1]) + '.dat')
            print(datos)
            print(ips)
            print('A la espera')
            try:
                conn, dirCli = sock.accept()
            except KeyboardInterrupt:
                print("Cancelado. Terminando ejecución")

            print('Conexion recibida de', dirCli)
            dt, dir = responderAConexion(conn, dirCli, ip)
            ips.add(dirCli)
            datos.add(dt)
            print('ips ' + str(ips))
            print('datos ' + str(datos))
            guardarDatos('../IoT_HoneyPot/IPsConectadas/puerto' + str(ip[1]) + '.dat', ips)
            guardarDatos('../IoT_HoneyPot/DatosObtenidos/puerto' + str(ip[1]) + '.dat', datos)
    except KeyboardInterrupt:
        print("Cancelado. Terminando ejecución")

main()