from uuid import UUID

from sqlalchemy.orm import Session

from app.database.models.audio import Audio
from app.database.models.transcript import Transcript


class TranscriptRepository:
    """
    Repository for transcript database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_audio(self, audio_id: UUID) -> Audio | None:
        return (
            self.db.query(Audio)
            .filter(Audio.id == audio_id)
            .first()
        )

    def create(self, transcript: Transcript) -> Transcript:
        self.db.add(transcript)
        self.db.commit()
        self.db.refresh(transcript)

        return transcript