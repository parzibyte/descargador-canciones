# descargador-canciones

Buscar y descargar canciones de YouTube ;)
# Modo de uso
Una vez que tengas Python, ejecuta el script. Las opciones son:

    main.py [-h] [--artista ARTISTA] archivo
## Descargar de un artista
Supongamos que tienes una lista de canciones de un artista (una por línea) en un archivo llamado **canciones.txt** así:

    Memory Motel
    Let me go

Y que deseas descargar el primer resultado. Las canciones son de *Rolling Stones* así que:

    python main.py --artista "Rolling Stones" canciones.txt

De este modo el script concatena el nombre del artista con cada canción del archivo, buscar en YT y descarga el primer resultado

Adicionalmente crea un directorio en donde coloca las canciones
## Descargar variadas
Si tienes un archivo txt con artista y título de canción, omite el artista. Supongamos que tienes un archivo llamado **lista.txt** así:

    David Bowie Ashes to ashes
    All along the watchtower jimi hendrix

Para descargarlos de variados usas:

    python main.py lista.txt

Eso no creará ningún directorio; descargará todas las canciones en el directorio actual


# Para el Luis del futuro...

Debes tener **ffmpeg** o algo así, se descarga y se instala. Luego se [agrega a la PATH](https://parzibyte.me/blog/2017/12/21/agregar-directorio-path-windows/) para que se pueda invocar desde cualquier lugar

Luego [instala Python y pip](https://parzibyte.me/blog/2019/10/08/instalar-python-pip-64-bits-windows/), más tarde instala **youtube-dl** con:

    pip install --upgrade youtube-dl

  

Ahora que lo tienes, ya puedes descargar una canción con:

  

    youtube-dl --extract-audio --audio-format mp3 url_youtube_aquí

  

Se puede descargar dependiendo de la búsqueda en YouTube, que es lo bueno para cuando no tenemos el link. Así:

    youtube-dl --extract-audio --audio-format mp3 "ytsearch1:aquí tu búsqueda"

  

En este caso `ytsearch1` va a descargar el primer resultado. `ytsearch2` descargaría 2 resultados, y así

  

Finalmente se puede renombrar la salida:

    youtube-dl --output "%(title)s.%(ext)s" --extract-audio --audio-format mp3 "ytsearch1:la búsqueda aquí"

  

# Más información: 

https://askubuntu.com/questions/643286/can-i-download-videos-from-a-youtube-search-query-using-youtube-dl

[https://github.com/ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl)
