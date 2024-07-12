import yt_dlp

# Define the URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=lKw6uqtGFfo&list=RDnQWFzMvCfLE&index=3"

# Create a yt-dlp object and download the video
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
