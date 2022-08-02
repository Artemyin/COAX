import os
import datetime
from moviepy.editor import VideoFileClip
import urllib


def video_to_gif(url):
    """Converts TikTok video to GIF.
    url -- address of TikTok video
    output -- parameter is path to GIF image
    """
    video_path = f"/tmp/{round(datetime.datetime.now().timestamp())}.mp4"
    output_path = video_path.split('/')[-1].replace("mp4", "gif")
    urllib.request.urlretrieve(url, video_path)
    videoClip = VideoFileClip(video_path)
    videoClip.write_gif(output_path, fps=24, program= 'ffmpeg')
    os.remove(video_path)
    return output_path
