import os
import sys
from pytube import YouTube

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <YouTube URL>")
        return

    link = sys.argv[1]
    yt = YouTube(link)

    # Print video details
    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # Define the target directory for the download
    script_dir = os.path.dirname(__file__)
    music_test_dir = os.path.join(script_dir, "Music_test")

    # Ensure the directory exists
    os.makedirs(music_test_dir, exist_ok=True)

    # Download the video to the "Music_test" directory
    yd.download(output_path=music_test_dir)

    print("Download completed successfully!")

if __name__ == "__main__":
    main()
