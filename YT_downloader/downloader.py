from pytube import YouTube
from sys import argv
import os

# Get the link from command line arguments
link = argv[1]
yt = YouTube(link)

# Print video details
print("Title: ", yt.title)
print("Views: ", yt.views)

# Get the highest resolution stream
yd = yt.streams.get_highest_resolution()

# Construct the path to the "Music_test" folder relative to the script location
current_dir = os.path.dirname(os.path.abspath(__file__))
music_test_dir = os.path.join(current_dir, "Music_test")

# Ensure the directory exists
os.makedirs(music_test_dir, exist_ok=True)

# Download the video to the "Music_test" directory
yd.download(output_path=music_test_dir)

print("Download completed successfully!")
