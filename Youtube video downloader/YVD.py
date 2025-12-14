from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)

        print("Video Downloaded Successfully")
    except Exception as e:
        print("Error:", e)

# IMPORTANT: use clean video URL (no &list=)
url = "https://www.youtube.com/watch?v=zT7niRUOs9o"
save_path = "./"

download_video(url, save_path)
