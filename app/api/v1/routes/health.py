from fastapi import APIRouter
from app.schemas.response import APIResponse

router = APIRouter(
    tags=["Health"],
)


@router.get(
    "/health",
    response_model=APIResponse,
    summary="Health Check",
)
async def health_check():
    """
    Check whether the API is running.
    """
    return APIResponse(
        success=True,
        message="API is healthy.",
        data={
            "service": "Ambient Clinical Scribe",
            "status": "healthy",
        },
    )