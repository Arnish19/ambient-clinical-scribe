from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


class SOAPNote(Base, TimestampMixin):
    """
    SOAP note generated from a transcript.
    """

    __tablename__ = "soap_notes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    transcript_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("transcripts.id"),
        unique=True,
        nullable=False,
    )

    soap_json: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    transcript = relationship(
        "Transcript",
        back_populates="soap_note",
    )