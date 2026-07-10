from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.constants.audio import (
    SUPPORTED_AUDIO_TYPES,
    SUPPORTED_EXTENSIONS,
)


def get_file_extension(filename: str) -> str:
    """
    Return the lowercase file extension.
    """
    return Path(filename).suffix.lower()


def is_supported_audio(upload_file: UploadFile) -> bool:
    """
    Validate both MIME type and file extension.
    """

    extension = get_file_extension(upload_file.filename)

    return (
        upload_file.content_type in SUPPORTED_AUDIO_TYPES
        and extension in SUPPORTED_EXTENSIONS
    )


def generate_unique_filename(filename: str) -> str:
    """
    Generate a UUID filename while preserving
    the original extension.
    """

    extension = get_file_extension(filename)

    return f"{uuid4()}{extension}"