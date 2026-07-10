from pathlib import Path
from uuid import UUID

from faster_whisper import WhisperModel
from sqlalchemy.orm import Session

from app.database.models.transcript import Transcript
from app.repositories.transcript_repository import TranscriptRepository


class WhisperService:
    """
    Handles speech-to-text using Faster Whisper.
    """

    def __init__(self, db: Session):
        self.repository = TranscriptRepository(db)

        # Load the model once
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
        )

    def transcribe(self, audio_id: UUID) -> Transcript:
        audio = self.repository.get_audio(audio_id)

        if audio is None:
            raise ValueError("Audio not found.")

        if not Path(audio.file_path).exists():
            raise FileNotFoundError("Audio file not found.")

        segments, info = self.model.transcribe(audio.file_path)

        transcript_text = " ".join(
            segment.text.strip()
            for segment in segments
        )

        transcript = Transcript(
            audio_id=audio.id,
            transcript=transcript_text,
            language=info.language,
        )

        return self.repository.create(transcript)