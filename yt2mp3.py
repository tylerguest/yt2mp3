import os
from pytube import YouTube
from pydub import AudioSegment

def download_and_convert_to_mp3(video_url, output_filename):
    try:
        # Download the YouTube video
        youtube = YouTube(video_url)
        video_stream = youtube.streams.filter(only_audio=True).first()
        video_stream.download(filename=f'{output_filename}.mp4')

        # Convert the video to MP3 using pydub
        audio = AudioSegment.from_file(f'{output_filename}.mp4', format="mp4")
        audio.export(f'{output_filename}.mp3', format="mp3")

        # Delete the mp4 file
        os.remove(f'{output_filename}.mp4')

        print("Video downloaded, converted to MP3, and mp4 file deleted successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Replace "YOUR_VIDEO_URL" with the actual YouTube video URL
    video_url = "https://www.youtube.com/watch?v=76U0gtuV9AY&ab_channel=ChromeforDevelopers"

    # Replace "output" with the desired output filename
    output_filename = "output"

    download_and_convert_to_mp3(video_url, output_filename)
