from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.soap import SOAPResponse
from app.services.soap.soap_service import SOAPService

router = APIRouter(
    prefix="/soap",
    tags=["SOAP"],
)


@router.post(
    "/{audio_id}",
    response_model=SOAPResponse,
    summary="Generate SOAP note",
)
def generate_soap(
    audio_id: UUID,
    db: Session = Depends(get_db),
):
    service = SOAPService(db)

    soap = service.generate(audio_id)

    return soap