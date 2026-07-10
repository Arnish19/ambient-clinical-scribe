from fastapi import APIRouter

from app.api.v1.routes.audio import router as audio_router
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.transcript import router as transcript_router

router = APIRouter()

router.include_router(health_router)
router.include_router(audio_router)
router.include_router(transcript_router)