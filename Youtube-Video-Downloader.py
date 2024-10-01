# import yt_dlp as youtube_dl
# import tkinter as tk
# from tkinter import filedialog

# # Function to download the video in highest quality
# def download_video(url, save_path):
#     # Options for yt-dlp to download the best video and audio and merge them
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',  # Download best video and best audio
#         'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save with title as filename
#         'merge_output_format': 'mp4',  # Merge video and audio into mp4 format
#     }

#     try:
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         print("Video downloaded successfully in the highest quality!")
#     except Exception as e:
#         print(f"Error occurred: {e}")

# # Function to open file dialog for selecting save directory
# def open_file_dialog():
#     folder = filedialog.askdirectory()
#     if folder:
#         print(f"Selected folder: {folder}")
#     return folder

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Hide the main Tkinter window

#     # Get the YouTube video URL from the user
#     video_url = input("Please enter a YouTube URL: ")
#     save_dir = open_file_dialog()  # Open the folder dialog to choose save location

#     if save_dir:
#         print("Started download...")
#         download_video(video_url, save_dir)  # Download the video in the highest quality
#     else:
#         print("Invalid save location.")


import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog

# Function to list available quality options and download based on user selection
def download_video(url, save_path):
    try:
        # Fetch available formats
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])

        # List available video formats with resolution and file size
        print("\nAvailable Quality Options:")
        format_list = []
        valid_index = 1
        for f in formats:
            if f['vcodec'] != 'none' and f.get('format_note') and f.get('filesize'):
                res = f.get('format_note', 'Unknown resolution')
                ext = f.get('ext', 'Unknown')
                file_size = f.get('filesize', 0)
                file_size_mb = file_size / (1024 * 1024) if file_size else 'Unknown size'
                format_list.append(f)
                print(f"{valid_index}. {res} | {ext.upper()} | {file_size_mb:.2f} MB")
                valid_index += 1

        # Ask user to select the format
        choice = int(input("\nEnter the number corresponding to the quality you want to download: ")) - 1
        if choice < 0 or choice >= len(format_list):
            print("Invalid selection. Exiting...")
            return

        selected_format = format_list[choice]
        print(f"Selected format: {selected_format['format_note']}")

        # Set options for downloading the selected quality
        ydl_opts = {
            'format': selected_format['format_id'],  # Download the user-selected format
            'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save with title as filename
        }

        # Download the selected video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
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
        print("Fetching available quality options...")
        download_video(video_url, save_dir)  # Download the video with user-selected quality
    else:
        print("Invalid save location.")
