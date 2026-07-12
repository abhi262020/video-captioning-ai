from pydantic import BaseModel


class CaptionResponse(BaseModel):

    video_id: str

    filename: str

    caption: str

    transcript: str

    confidence: float

    processing_time: float