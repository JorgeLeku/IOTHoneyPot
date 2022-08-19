import sys
import socket
import random
import pickle
sys.path.append('../API/')
from apiArchivos import leerDatos, guardarDatos

sck = socket.socket()
host = socket.gethostname()

def main ():
    respuestasPredefinidas = leerDatos('../IoT_Device_Searcher/datos/datosRespuestasPorDefecto.dat')
    ipsDetectadas = leerDatos('../IoT_HoneyPot/IPsConectadas/puerto8081.dat')
    
    sck.bind((host, 8081))
    
    try:
        while True:
            direcc, respuesta = random.choice(list(respuestasPredefinidas.items()))
            conn, direcc = sck.accept()
            print('IP '+ direcc + ' se ha conectado')
            msg = conn.recv(16384)
            print('Mensaje recibido: ' + msg)
            ipsDetectadas.add(str(msg))
            if b'login.cgi' in msg:
                print('Intento de login')
                print('IP: ' + str(direcc) + 'Respuesta: ' + str(respuesta))
                conn.send(respuesta.content)
            conn.close()
    except KeyboardInterrupt:
        print('Interrumpido')
    guardarDatos('../IoT_HoneyPot/IPsConectadas/puerto8081.dat', ipsDetectadas)
main()
