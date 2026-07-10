from __future__ import annotations

import uuid

from sqlalchemy import BigInteger, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.enums import AudioStatus
from app.database.mixins import TimestampMixin

from sqlalchemy.orm import relationship

class Audio(Base, TimestampMixin):
    """
    Represents an uploaded audio file.
    """

    __tablename__ = "audio_files"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    content_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[AudioStatus] = mapped_column(
        Enum(AudioStatus),
        default=AudioStatus.UPLOADED,
        nullable=False,
    )

    transcript = relationship(
        "Transcript",
        back_populates="audio",
        uselist=False,
    )