from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories.icd_repository import ICDRepository
from app.repositories.report_repository import ReportRepository
from app.utils.pdf_generator import PDFGenerator


class ReportService:
    """
    Generates a complete PDF report.
    """

    def __init__(self, db: Session):
        self.repository = ReportRepository(db)
        self.icd_repository = ICDRepository()

    def generate(self, audio_id: UUID):

        data = self.repository.get_report_data(audio_id)

        if data is None:
            raise ValueError("Report data not found.")

        soap_json = data["soap"].soap_json

        assessment = soap_json.get("assessment", "")

        # Reuse the ICD repository directly for now.
        # Later we can call ICDService if needed.
        icd = self.icd_repository.search(
            assessment,
            limit=5,
        )

        report = {
            "transcript": data["transcript"].transcript,
            "soap": soap_json,
            "icd": icd,
        }

        return PDFGenerator.generate(report)