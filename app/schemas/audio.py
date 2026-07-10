from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.database.enums import AudioStatus


class AudioUploadResponse(BaseModel):
    """
    Response returned after a successful audio upload.
    """

    id: UUID
    original_filename: str
    stored_filename: str
    content_type: str
    file_size: int
    status: AudioStatus
    created_at: datetime

    model_config = {
        "from_attributes": True
    }