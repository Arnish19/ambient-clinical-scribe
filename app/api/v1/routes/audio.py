from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.audio import AudioUploadResponse
from app.services.audio.upload_service import AudioService

router = APIRouter(
    prefix="/audio",
    tags=["Audio"],
)


@router.post(
    "/upload",
    response_model=AudioUploadResponse,
    summary="Upload an audio file",
)
async def upload_audio(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Upload an audio file.
    """

    service = AudioService(db)

    audio = await service.upload_audio(file)

    return audio