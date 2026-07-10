from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.transcript import TranscriptResponse
from app.services.transcript.whisper_service import WhisperService

router = APIRouter(
    prefix="/transcript",
    tags=["Transcript"],
)


@router.post(
    "/{audio_id}",
    response_model=TranscriptResponse,
    summary="Generate transcript using Whisper",
)
def generate_transcript(
    audio_id: UUID,
    db: Session = Depends(get_db),
):
    service = WhisperService(db)

    transcript = service.transcribe(audio_id)

    return transcript