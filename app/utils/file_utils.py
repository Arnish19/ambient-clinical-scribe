from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.constants.audio import (
    SUPPORTED_AUDIO_TYPES,
    SUPPORTED_EXTENSIONS,
)
from app.core.config import settings


def get_file_extension(filename: str) -> str:
    return Path(filename).suffix.lower()


def is_supported_audio(file: UploadFile) -> bool:
    extension = get_file_extension(file.filename)

    return (
        extension in SUPPORTED_EXTENSIONS
        and file.content_type in SUPPORTED_AUDIO_TYPES
    )


def generate_unique_filename(filename: str) -> str:
    extension = get_file_extension(filename)
    return f"{uuid4()}{extension}"


def get_upload_path(filename: str) -> Path:
    upload_dir = Path(settings.UPLOAD_DIRECTORY)

    upload_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    return upload_dir / filename