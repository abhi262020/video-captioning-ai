import subprocess
import os


AUDIO_DIR = "processed/audio"

os.makedirs(
    AUDIO_DIR,
    exist_ok=True
)


def extract_audio(
    video_path: str
):

    audio_path = (
        f"{AUDIO_DIR}/audio.wav"
    )


    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-vn",
        "-acodec",
        "pcm_s16le",
        audio_path,
        "-y"
    ]


    subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


    return audio_path