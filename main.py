"""
Para el Luis del futuro...
Debes tener ffmpeg o algo así, se descarga y se instala. Luego se agrega a la PATH para que se pueda invocar desde cualquier lugar
Luego instala Python y pip, más tarde instala youtube_dl con:
    pip install --upgrade youtube-dl

Ahora que lo tienes, ya puedes descargar una canción con:

    youtube-dl --extract-audio --audio-format mp3 url_youtube_aquí

Se puede buscar también, que es lo bueno para cuando no tenemos el link. Así:
    youtube-dl --extract-audio --audio-format mp3 "ytsearch1:aquí tu búsqueda"

    En este caso ytsearch1 va a descargar el primer resultado. ytsearch2 descargaría 2 resultados, y así

Finalmente se puede renombrar la salida:
    youtube-dl --output "%(title)s.%(ext)s" --extract-audio --audio-format mp3 "ytsearch1:la búsqueda aquí"

Más información: https://askubuntu.com/questions/643286/can-i-download-videos-from-a-youtube-search-query-using-youtube-dl
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
        nombre_salida = nombre_salida + ".mp3"

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
