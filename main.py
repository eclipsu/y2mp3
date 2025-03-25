from pytubefix import YouTube, Search
import os
from pathlib import Path
import sys

# Files will be downloaded to downloads folder in user's home directory
DOWNLOAD_FOLDER = Path.home() / "Downloads" / "Music"
DOWNLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    clear()
    print("=" * 50)
    print(" FAST YOUTUBE TO MP3 ".center(50, "="))
    print("=" * 50)
    print(f"Download Location: {DOWNLOAD_FOLDER}\n")

def download_song(song_title):
    print(f"Searching for: {song_title}\n")
    
    results = Search(song_title)
    if not results.videos:
        print("[ERROR] No results found. Try another search.")
        return

    yt = YouTube(results.videos[0].watch_url)
    length = f"{results.videos[0].length // 60}:{results.videos[0].length % 60:02d}"
    
    print("+" + "-" * 48 + "+")
    print(f"| {'Title:':<10} {yt.title[:35]:<35} |")
    print(f"| {'Author:':<10} {yt.author[:35]:<35} |")
    print(f"| {'Duration:':<10} {length:<35} |")
    print("+" + "-" * 48 + "+")

    video = yt.streams.filter(only_audio=True).first()
    
    print("\n[INFO] Downloading...")
    out_file = video.download(output_path=DOWNLOAD_FOLDER)
    
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    
    print(f"[SUCCESS] Download Complete: {yt.title}\n")
    print("=" * 50)

if len(sys.argv) > 1:
    song_title = " ".join(sys.argv[1:])
    try:
        download_song(song_title)
    except Exception as e:
        print(f"[ERROR] {e}\n")
    sys.exit()

while True:
    title()
    song_title = input("Enter the Song Name (or type 'EXIT' to quit):\n>> ")
    
    if song_title.strip().upper() == "EXIT":
        print("\n[EXIT] Have a great day!\n")
        break
    
    try:
        download_song(song_title)
    except Exception as e:
        print(f"[ERROR] {e}\n")