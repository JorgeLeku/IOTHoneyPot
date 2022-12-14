import pickle

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
    
def leerDatosTxt(nArch):
    archivo = open(nArch, "r")
    datos = archivo.read()

    lista = datos.split(",")
    archivo.close()
    return lista
