"""

    Programado por Luis Cabrera Benito 
  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
    
    Blog:       https://parzibyte.me/blog
    Ayuda:      https://parzibyte.me/blog/contrataciones-ayuda/
    Contacto:   https://parzibyte.me/blog/contacto/
"""
from subprocess import check_output
import argparse
import time
import math
import os


def crear_directorio_si_no_existe(directorio):
    if not os.path.exists(directorio):
        os.makedirs(directorio)


def leyenda_segundos(segundos):
    if segundos < 60:
        return str(math.floor(segundos)) + " segundos"
    minutos = math.floor(segundos / 60)
    segundos = math.floor(segundos % 60)
    cadena = "{} minuto".format(minutos)
    if minutos != 1:
        cadena = cadena + "s"
    if segundos > 0:
        cadena = cadena + (" {} segundo".format(segundos))
        if segundos != 1:
            cadena = cadena + "s"
    return cadena


parser = argparse.ArgumentParser()
parser.add_argument(
    "archivo", help="El archivo que contiene la lista de canciones o canciones y artista")
parser.add_argument("--artista", type=str,
                    help="Si está presente, se descargarán las canciones de 'archivo' de ese artista; si no, se descargarán tal y como están en el archivo")
argumentos = parser.parse_args()

artista = ""
archivo = argumentos.archivo
directorio = "./"
nombre_salida = ""
if argumentos.artista:
    artista = argumentos.artista + " "  # un espacio para la búsqueda
    print("OK, todas las canciones en {} son del artista {}".format(archivo, artista))
    print("Creando directorio de artista...")
    crear_directorio_si_no_existe("./" + artista)
    directorio = "./"+argumentos.artista
    nombre_salida = "\"%(title)s.%(ext)s\""
tiempo_inicio = time.time()
contador = 0
with open(archivo) as lista:
    for linea in lista:
        linea_sin_salto = linea.rstrip()
        busqueda = artista + linea_sin_salto
        nombre_salida = linea_sin_salto
        if argumentos.artista:
            nombre_salida = directorio + "/" + linea_sin_salto
        else:
            nombre_salida = linea_sin_salto
        nombre_salida = nombre_salida + ".%(ext)s"

        print("Buscando '{}'... ".format(busqueda), end="")
        comando = """youtube-dl --output \"""" + nombre_salida + \
            """\" --extract-audio --audio-format mp3 \"ytsearch1:{}\"""".format(
                busqueda)
        check_output(comando)
        print("[OK]")
        contador = contador + 1
tiempo_transcurrido = time.time() - tiempo_inicio
print("Se han descargado {} canciones en {}".format(
    contador, leyenda_segundos(tiempo_transcurrido)))
