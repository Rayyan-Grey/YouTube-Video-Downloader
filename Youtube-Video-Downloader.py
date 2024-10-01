import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog

# Function to download the video in highest quality
def download_video(url, save_path):
    # Options for yt-dlp to download the best video and audio and merge them
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and best audio
        'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save with title as filename
        'merge_output_format': 'mp4',  # Merge video and audio into mp4 format
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully in the highest quality!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Function to open file dialog for selecting save directory
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Get the YouTube video URL from the user
    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()  # Open the folder dialog to choose save location

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)  # Download the video in the highest quality
    else:
        print("Invalid save location.")


