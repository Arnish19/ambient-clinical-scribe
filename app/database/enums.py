from enum import Enum


class AudioStatus(str, Enum):
    """
    Processing status of uploaded audio.
    """

    UPLOADED = "uploaded"
    TRANSCRIBING = "transcribing"
    COMPLETED = "completed"
    FAILED = "failed"