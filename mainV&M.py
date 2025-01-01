import sys
import signal
import yt_dlp as youtube_dl

def ctrl_c(sig, frame):
    print("\n[!] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

if len(sys.argv) < 2 or sys.argv[1] == "":
    print("[!] Introduce el ID del video")
    sys.exit(1)
else:
    video_id = sys.argv[1]
    url = f"https://www.youtube.com/watch?v={video_id}"

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Descargar video y audio de la mejor calidad
            'quiet': False,  # Muestra información del progreso
            'outtmpl': '%(title)s.%(ext)s',  # Guarda el archivo con el título del video
            'merge_output_format': 'mp4',  # Formato final de salida
        }

        print(f"[+] Descargando videoclip de: {url}")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("[+] Descarga completada con éxito.")

    except Exception as e:
        print(f"[!] Error al descargar el video: {e}")