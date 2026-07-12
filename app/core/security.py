from fastapi import HTTPException


ALLOWED_VIDEO_TYPES = [
    "video/mp4",
    "video/mpeg",
    "video/webm"
]


def validate_video_type(
    content_type: str
):

    if content_type not in ALLOWED_VIDEO_TYPES:

        raise HTTPException(
            status_code=400,
            detail="Unsupported video format"
        )


    return True