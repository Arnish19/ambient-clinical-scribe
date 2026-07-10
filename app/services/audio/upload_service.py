from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.enums import AudioStatus
from app.database.models.audio import Audio
from app.repositories.audio_repository import AudioRepository
from app.utils.file_utils import (
    generate_unique_filename,
    get_upload_path,
    is_supported_audio,
)


class AudioService:
    """
    Handles audio upload business logic.
    """

    def __init__(self, db: Session):
        self.repository = AudioRepository(db)

    async def upload_audio(self, file: UploadFile) -> Audio:
        """
        Validate, save and persist uploaded audio.
        """

        if not file.filename:
            raise ValueError("Filename is missing.")

        if not is_supported_audio(file):
            raise ValueError("Unsupported audio format.")

        stored_filename = generate_unique_filename(file.filename)

        upload_path = get_upload_path(stored_filename)

        content = await file.read()

        max_size = settings.MAX_AUDIO_SIZE_MB * 1024 * 1024

        if len(content) > max_size:
            raise ValueError(
                f"File exceeds {settings.MAX_AUDIO_SIZE_MB} MB limit."
            )

        with open(upload_path, "wb") as buffer:
            buffer.write(content)

        audio = Audio(
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_path=str(upload_path),
            file_size=len(content),
            content_type=file.content_type,
            status=AudioStatus.UPLOADED,
        )

        return self.repository.create(audio)