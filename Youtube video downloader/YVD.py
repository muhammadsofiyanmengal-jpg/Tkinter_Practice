import yt_dlp as yd

def download_video(url, save_path):
        video = {
            'output' : './',
            'format' : 'mp4'
            }
        with yd.YoutubeDL(video) as ydl:
            ydl.download(url)

        
        
# IMPORTANT: use clean video URL (no &list=)

url = "https://www.youtube.com/watch?v=zT7niRUOs9o"
save_path = "./"

download_video(url, save_path)
