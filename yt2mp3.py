import os
from pytube import YouTube
from pydub import AudioSegment

def download_and_convert_to_mp3(video_url):
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

        print("Video downloaded, converted to MP3, and mp4 file deleted successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Take user input for the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    download_and_convert_to_mp3(video_url)
