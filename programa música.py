from pytube import YouTube
from pytube import Playlist

def descargarCancion(url:str):
    youtube= YouTube(url)
    youtube.author
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

def descargarLista(url:str):
    playlist=Playlist(url)
    for cancion in playlist.videos:
        print("Descargando canción: ", cancion.title)
        cancion.streams.get_audio_only().download("canciones/")
        print("**********************************\n")
url= "https://www.youtube.com/playlist?list=PL68B86C1DFA80AA8F"


#descargarCancion("https://www.youtube.com/watch?v=JponLczaj4o")
descargarLista(url)