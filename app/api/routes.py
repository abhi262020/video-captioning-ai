from fastapi import APIRouter, UploadFile, File
from app.schemas.response import CaptionResponse
from app.utils.file_utils import save_upload_file
import uuid
import time

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post(
    "/caption",
    response_model=CaptionResponse
)
async def generate_caption(
    video: UploadFile = File(...)
):

    start_time = time.time()

    # Save uploaded file
    file_path, filename = save_upload_file(video)

    processing_time = round(
        time.time() - start_time,
        2
    )

    return CaptionResponse(
        video_id=str(uuid.uuid4()),
        filename=filename,
        caption="Video uploaded successfully.",
        transcript="Transcript generation will be implemented next.",
        confidence=1.0,
        processing_time=processing_time
    )