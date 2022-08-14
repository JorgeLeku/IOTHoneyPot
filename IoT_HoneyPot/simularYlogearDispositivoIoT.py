import sys
import socket
import random
import pickle
sys.path.append('../API/')
from apiArchivos import leerDatos, guardarDatos

sck = socket.socket()
host = socket.gethostname()

def loadData(filename):
    pickleFile = open(filename, 'rb')
    obj = pickle.load(pickleFile)
    pickleFile.close()
    return obj

def main ():
    login_cgi = loadData('../IoT_HoneyPot/port_8081.dat')
    address, response = random.choice(list(login_cgi.items()))
    print (address)
    print(response)
    sck.bind((host, puerto))
    
    try:
        while true:
            conn, direcc = sck.accept()
            print('IP '+ direcc + ' se ha conectado')
            msg = conn.recv()
            print('Mensaje recibido: ' + msg)
            
    except KeyboardInterrupt:
        print('Interrumpido')
main()