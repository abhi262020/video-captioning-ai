import whisper


model = whisper.load_model(
    "base"
)


def generate_transcript(video):

    result = model.transcribe(
        video
    )

    return result["text"]