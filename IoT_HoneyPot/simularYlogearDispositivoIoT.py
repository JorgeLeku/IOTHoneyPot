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
        dt =+ dato
        print('dato {!r}'.format(dato))
        if dato:
            print('Respondiendo al cliente')
            dir, response = random.choice(list(respuestas.items()))
            connection.sendall(response.content)
        else:
            print('sin datos del cliente', client_address)
            break
    return(dt, dato)

def main():
    ip = inicializarDatos()
    try:
        while True:
            datos = leerDatos('../IoTHoneyPot/DatosObtenidos/puerto' + ip + '.dat')
            ips = leerDatos('../IoTHoneyPot/IPsConectadas/puerto' + ip + '.dat')
            print('A la espera')
            conn, dirCli = sock.accept()
            ips.add(dir)
            print('Conexion recivida de', dirCli)
            dt, dato = responderAConexion(conn, dirCli, ip, datos)
            datos.add(dato)
            guardarDatos('../IoTHoneyPot/IPsConectadas/puerto' + ip + '.dat', ips)
            guardarDatos('../IoTHoneyPot/DatosObtenidos/puerto' + ip + '.dat', dt)
    except KeyboardInterrupt:
        print("Cancelado. Terminando ejecución")

main()