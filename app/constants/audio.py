"""
Audio upload configuration constants.
"""

SUPPORTED_AUDIO_TYPES = {
    "audio/mpeg",      # .mp3
    "audio/wav",       # .wav
    "audio/x-wav",     # .wav
    "audio/mp4",       # .m4a
    "audio/x-m4a",     # .m4a
    "audio/flac",      # .flac
}

SUPPORTED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".flac",
}

DEFAULT_MAX_AUDIO_SIZE_MB = 100