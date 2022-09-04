# IOTHoneyPot
> Un sistema de busqueda y simulacion de dispositios IoT

## Contenidos
- API
- Buscador de dispositivos
- HoneyPot IoT

## Ejecutar
### En caso de ejecutar los vagranfile
Modificar dichos vagrantfile con los datos deseados

### Ejecucion normal
#### Buscador de Dispositivos
Insertar IPs que se desean Ignorar en:
```
IPsAIgnorar.txt
```
Insertar puertos en los que buscar en:
```
PuertosABuscar.txt
```
Lanzar comando 
```shell
python .\buscarDispositivosIOT.py
```
#### HoneyPot IoT
Lanzar comando sustituyendo la IP y el puerto sobre los que vamos a escuchar:
```
 python .\simularYlogearDispositivoIoT.py ip puerto
```