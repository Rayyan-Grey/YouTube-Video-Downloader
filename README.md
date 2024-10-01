# YouTube Video Downloader

A simple Python tool that allows users to download videos from YouTube in the highest quality using `yt-dlp`. This downloader merges the best video and audio streams into a single MP4 file.

## Features
- Download videos in the highest available quality.
- Automatically merges audio and video streams.
- User-friendly interface for selecting the download location.

## Requirements
Before running the script, ensure that you have the following installed:

- **Python 3.x**
- **yt-dlp**: Install using:
  ```bash
  pip install yt-dlp
Tkinter: Should come pre-installed with Python. If not, follow the platform-specific installation:

Linux: sudo apt-get install python3-tk

MacOS: Already included in Python installations.

Windows: Installed with Python by default.

FFmpeg: Make sure FFmpeg is installed and added to your system PATH for merging audio and video streams. You can download it from FFmpeg's official website.

# How to Use
- Clone the Repository: Clone this repository to your local machine using:
```bash
git clone https://github.com/Rayyan-Grey/YouTube-Video-Downloader.git
```
- Run the Script: Navigate to the project directory and run the Python script:
```bash
python Youtube-Video-Downloader.py
```
- Follow the Prompts:

  - Enter the YouTube video URL when prompted.
  - Choose the folder where you want the video to be saved.
    
- Download Completion: The selected video will be downloaded, and the audio will be merged into a single MP4 file.

# Example
```bash
Please enter a YouTube URL: https://www.youtube.com/watch?v=example
Selected folder: C:\Users\Downloads
Started download...
Video downloaded successfully in the highest quality!
```
# Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.
