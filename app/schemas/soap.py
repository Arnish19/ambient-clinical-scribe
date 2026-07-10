from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SOAPResponse(BaseModel):
    id: UUID
    transcript_id: UUID
    soap_json: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }