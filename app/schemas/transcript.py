from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class TranscriptResponse(BaseModel):
    id: UUID
    audio_id: UUID
    transcript: str
    language: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }