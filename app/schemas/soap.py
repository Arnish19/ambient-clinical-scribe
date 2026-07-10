from datetime import datetime
from uuid import UUID
from typing import Any

from pydantic import BaseModel


class SOAPResponse(BaseModel):
    id: UUID
    transcript_id: UUID
    soap_json: dict[str, Any]
    created_at: datetime

    model_config = {
        "from_attributes": True
    }