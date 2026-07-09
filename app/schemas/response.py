from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):
    """
    Standard API response model.
    """

    success: bool
    message: str
    data: Any | None = None