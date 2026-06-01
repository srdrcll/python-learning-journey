import yt_dlp
import os

url = input("Enter url: ")

# Target folder path for the download (leaves empty to save in the project directory)
download_path = ""

try:
    ydl_opts = {
        'outtmpl': os.path.join(download_path, "%(title)s.%(ext)s"),
        # Displays the download progress and statistics in the terminal
        'quiet': False,
        'nocheckcertificate': True,
        'extractor_args': {'youtube': {'player_client': ['ios','android']}},
        'check_formats': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download complete")

except Exception as e:
    print(f"Error: {e}")