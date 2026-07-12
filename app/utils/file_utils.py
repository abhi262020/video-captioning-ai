import os
import shutil
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_upload_file(upload_file: UploadFile):

    # Get file extension
    extension = os.path.splitext(upload_file.filename)[1]

    # Generate unique filename
    filename = f"{uuid.uuid4()}{extension}"

    # Full path
    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            upload_file.file,
            buffer
        )

    # Return exactly TWO values
    return file_path, filename