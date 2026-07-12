import whisper


class WhisperModel:

    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, video_path: str) -> str:

        result = self.model.transcribe(video_path)

        return result["text"]


whisper_model = WhisperModel()