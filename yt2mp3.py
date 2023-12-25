import os
from tkinter import Tk, Label, Entry, Button, StringVar
from pytube import YouTube
from pydub import AudioSegment

def download_and_convert_to_mp3():
    video_url = url_entry.get()

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

        result_label.config(text="Video downloaded and converted to MP3 successfully!")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
root = Tk()
root.title("YouTube to MP3 Converter")

# Create and place widgets
Label(root, text="Enter YouTube video URL:").grid(row=0, column=0, padx=10, pady=10)

url_var = StringVar()
url_entry = Entry(root, textvariable=url_var, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

convert_button = Button(root, text="Convert to MP3", command=download_and_convert_to_mp3)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
