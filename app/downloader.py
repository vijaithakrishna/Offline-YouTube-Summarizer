import yt_dlp
import os
import uuid

def download_audio(url: str) -> str:
    output_dir = "/app/downloads"
    os.makedirs(output_dir, exist_ok=True)

    unique_id = uuid.uuid4().hex[:8]
    temp_path = f"{output_dir}/{unique_id}.%(ext)s"

    final_file = {"path": None}

    def pp_hook(d):
        if d["status"] == "finished":
            final_file["path"] = d["info_dict"]["filepath"]

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": temp_path,
        "quiet": False,
        "postprocessor_hooks": [pp_hook],
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return final_file["path"]
