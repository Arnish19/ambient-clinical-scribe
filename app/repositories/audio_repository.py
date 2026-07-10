from sqlalchemy.orm import Session

from app.database.models.audio import Audio


class AudioRepository:
    """Repository for audio database operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, audio: Audio) -> Audio:
        """
        Save audio metadata to the database.
        """
        self.db.add(audio)
        self.db.commit()
        self.db.refresh(audio)

        return audio