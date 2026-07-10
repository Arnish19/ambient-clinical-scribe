from uuid import UUID

from sqlalchemy.orm import Session

from app.database.models.soap_note import SOAPNote
from app.database.models.transcript import Transcript


class SOAPRepository:
    """
    Repository for SOAP note database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_transcript_by_audio(self, audio_id: UUID) -> Transcript | None:
        return (
            self.db.query(Transcript)
            .filter(Transcript.audio_id == audio_id)
            .first()
        )

    def create(self, soap_note: SOAPNote) -> SOAPNote:
        self.db.add(soap_note)
        self.db.commit()
        self.db.refresh(soap_note)

        return soap_note