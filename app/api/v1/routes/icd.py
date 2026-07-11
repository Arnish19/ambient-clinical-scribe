from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.icd import ICDResponse
from app.services.icd.icd_service import ICDService

router = APIRouter(
    prefix="/icd",
    tags=["ICD-10"],
)


@router.post(
    "/{audio_id}",
    response_model=ICDResponse,
)
def recommend_icd(
    audio_id: UUID,
    db: Session = Depends(get_db),
):

    service = ICDService(db)

    return service.recommend(audio_id)