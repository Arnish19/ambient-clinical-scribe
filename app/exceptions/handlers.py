from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import AudioUploadException


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register custom exception handlers.
    """

    @app.exception_handler(AudioUploadException)
    async def audio_upload_exception_handler(
        request: Request,
        exc: AudioUploadException,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": exc.message,
                "data": None,
            },
        )