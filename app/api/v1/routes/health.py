from fastapi import APIRouter

router = APIRouter(
    tags=["Health"],
)


@router.get(
    "/health",
    summary="Health Check",
)
async def health_check():
    """
    Check whether the API is running.
    """
    return {
        "status": "healthy",
        "service": "Ambient Clinical Scribe",
    }