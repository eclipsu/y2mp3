from pytubefix import YouTube, Search
import os
from pathlib import Path


# Files will be downloaded to downloads folder in user's home directory
# Create the downloads folder if it doesn't exist
DOWNLOAD_FOLDER = Path.home() / "Downloads" / "Music"
DOWNLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

print("\n🎵 Fast Youtube to Mp3 🎵")
print("===================================")
print("Downloaded files will be saved in: ", DOWNLOAD_FOLDER)
print("Type 'EXIT' to stop the program.\n")

while True:
    # Get user input
    song_title = input("Enter the Song Name (or type 'EXIT' to quit): \n>> ")

    # Check for exit condition
    if song_title.strip().upper() == "EXIT":
        print("\n BYEE! Have a great day! 🎶\n")
        break

    try:
        # Initialize YouTube object
        results = Search(song_title)
        yt = YouTube(results.videos[0].watch_url)
        

        length = f"{results.videos[0].length // 60}:{results.videos[0].length % 60:02d}"
        print(f"\n🔍 Fetching song: {results.videos[0].title} by {results.videos[0].author} ({length})")

        video = yt.streams.filter(only_audio=True).first()

        print("📥 Downloading...")
        out_file = video.download(output_path=DOWNLOAD_FOLDER)

        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

        print(f"✅ '{yt.title}' has been successfully downloaded!\n")
        print("===================================")

    except Exception as e:
        print(f"❌ Error: {e}\nPlease try again.\n")
