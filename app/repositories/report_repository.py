from uuid import UUID

from sqlalchemy.orm import Session

from app.database.models.audio import Audio
from app.database.models.transcript import Transcript


class ReportRepository:
    """
    Repository for fetching all data required for report generation.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_report_data(self, audio_id: UUID):

        audio = (
            self.db.query(Audio)
            .filter(Audio.id == audio_id)
            .first()
        )

        if audio is None:
            return None

        transcript = (
            self.db.query(Transcript)
            .filter(Transcript.audio_id == audio_id)
            .first()
        )

        if transcript is None:
            return None

        if transcript.soap_note is None:
            return None

        return {
            "audio": audio,
            "transcript": transcript,
            "soap": transcript.soap_note,
        }