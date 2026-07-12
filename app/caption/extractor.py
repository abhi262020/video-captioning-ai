import os
import cv2
import tempfile
from app.caption.whisper import transcribe_audio

def extract_video_context(video_path: str):
    """
    Extract key frames and transcript from a video.
    """

    cap = cv2.VideoCapture(video_path)

    frames = []
    count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save one frame every 60 frames
        if count % 60 == 0:
            temp = tempfile.NamedTemporaryFile(
                suffix=".jpg",
                delete=False
            )

            cv2.imwrite(temp.name, frame)
            frames.append(temp.name)

        count += 1

    cap.release()

    transcript = transcribe_audio(video_path)

    return {
        "frames": frames,
        "transcript": transcript
    }