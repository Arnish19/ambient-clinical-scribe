from pathlib import Path
from uuid import UUID

from openai import OpenAI
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.models.transcript import Transcript
from app.repositories.transcript_repository import TranscriptRepository


class WhisperService:
    """
    Handles speech-to-text using OpenAI Whisper.
    """

    def __init__(self, db: Session):
        self.repository = TranscriptRepository(db)
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def transcribe(self, audio_id: UUID) -> Transcript:

        audio = self.repository.get_audio(audio_id)

        if audio is None:
            raise ValueError("Audio not found.")

        with open(Path(audio.file_path), "rb") as file:

            result = self.client.audio.transcriptions.create(
                model=settings.WHISPER_MODEL,
                file=file,
            )

        transcript = Transcript(
            audio_id=audio.id,
            transcript=result.text,
            language="en",
        )

        return self.repository.create(transcript)