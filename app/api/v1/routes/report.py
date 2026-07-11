from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from io import BytesIO

from app.database.session import get_db
from app.services.report.report_service import ReportService

router = APIRouter(
    prefix="/report",
    tags=["Report"],
)


@router.get("/{audio_id}")
def generate_report(
    audio_id: UUID,
    db: Session = Depends(get_db),
):

    service = ReportService(db)

    pdf = service.generate(audio_id)

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition": 'attachment; filename="clinical_report.pdf"'
        },
    )