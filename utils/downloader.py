import yt_dlp
import os
import uuid

def download_video(url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    video_id = str(uuid.uuid4())
    output_path = os.path.join(output_dir, f"{video_id}.mp4")

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': output_path,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_path
