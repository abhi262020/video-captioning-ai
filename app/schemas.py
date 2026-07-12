from pydantic import BaseModel


class CaptionRequest(BaseModel):
    style: str


class CaptionResponse(BaseModel):
    style: str
    caption: str