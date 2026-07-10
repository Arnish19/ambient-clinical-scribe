class AudioUploadException(Exception):
    """
    Base exception for audio upload errors.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class UnsupportedAudioFormatException(AudioUploadException):
    """
    Raised when an unsupported audio format is uploaded.
    """


class FileTooLargeException(AudioUploadException):
    """
    Raised when the uploaded file exceeds the maximum allowed size.
    """


class EmptyFileException(AudioUploadException):
    """
    Raised when the uploaded file is empty.
    """