import PySimpleGUI as sg
import threading
from pytube import YouTube
from pydub import AudioSegment
import os

# Define the layout of the GUI
layout = [
    [sg.Text("Enter YouTube video URL:")],
    [sg.Input(key="url")],
    [sg.Text("", key="status")],
    [sg.Button("Convert to MP3"), sg.Exit()],
    [sg.ProgressBar(orientation="horizontal", size=(50, 20), max_value=100, key="progress")]
]

# Create the window
window = sg.Window("YouTube to MP3 Converter", layout)

# Define the function to download and convert the video
def download_and_convert_to_mp3():
    video_url = window["url"].get()

    try:
        # Download the YouTube video
        youtube = YouTube(video_url)
        video_title = youtube.title  # Extract the video title

        video_stream = youtube.streams.filter(only_audio=True).first()
        video_stream.download(filename=f'{video_title}.mp4')

        # Convert the video to MP3 using pydub
        audio = AudioSegment.from_file(f'{video_title}.mp4', format="mp4")
        audio.export(f'{video_title}.mp3', format="mp3")

        # Delete the mp4 file
        os.remove(f'{video_title}.mp4')

        # Update the status text
        window.write_event_value('update_status', f"Video downloaded and converted to MP3 successfully!")

        # Update the progress bar
        window.write_event_value('update_progress', 100)

    except Exception as e:
        # Update the status text
        window.write_event_value('update_status', f"Error: {str(e)}")

        # Update the progress bar
        window.write_event_value('update_progress', 0)

# Define the event loop
while True:
    event, values = window.read()

    if event == "Convert to MP3":
        # Clear the status text
        window["status"].update("")

        # Start a new thread to download and convert the video
        threading.Thread(target=download_and_convert_to_mp3).start()

    elif event == "update_status":
        # Update the status text
        window["status"].update(values[event])

    elif event == "update_progress":
        # Update the progress bar
        window["progress"].update(values[event])

    elif event == "Exit" or event is None:
        break

# Close the window
window.close()