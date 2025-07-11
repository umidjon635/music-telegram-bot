from yt_dlp import YoutubeDL
import os

def download_mp3_from_youtube(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)
        filename = ydl.prepare_filename(info['entries'][0])
        mp3_file = filename.replace(".webm", ".mp3").replace(".m4a", ".mp3")
        return mp3_file


def search_music():
    return None