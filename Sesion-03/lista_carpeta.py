import os
import time

# Variables
# carpeta = "/home/rctorr/CursoPython/Sesion-03"
carpeta = "."  # Carpeta actual

def obtener_elementos(carpeta):
    """
    Obtiene los elementos de la carpeta y regresa en forma de lista
    """
    # Obtener la lista de elemento de un carpeta
    nombres = os.listdir(carpeta)  # ["nom1", "nom2", ...]

    """
    Estructura de datos para incluir el tamaño
    [
        ["nom1", 1234],  <- e[0], e[1]
        ["nom2", 5678],
        ...
    ]
    """
    elementos = []
    total = 0
    for nom in nombres:
        if os.path.isfile(nom):  # si es un archivo?
            tam = os.path.getsize(nom)
        else: # es una carpeta
            tam = 0

        # Obtener la fecha
        fecha = os.path.getmtime(nom)
        fecha = time.ctime(fecha)

        elemento = [nom, tam, fecha]
        elementos.append(elemento)
        
        # sumar el tam a total para cada elemento
        total += tam  # total = total + tam
    
    return elementos, total

def imprimir_elementos(elementos, total):
    """
    Imprime la lista de elementos en formato texto en la salida
    estándar.
    """
    # Imprimir la lista
    for e in elementos:
        # print("{} {}".format(e[0], e[1])
        print("{:30} {:10} {:15}".format(*e))
    # Imprime toal
    print("-" * 40)
    print("Total: {} bytes".format(total))
    
    
# Llamando a las funciones
elementos, total = obtener_elementos(carpeta)
imprimir_elementos(elementos, total)

