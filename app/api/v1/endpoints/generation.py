from fastapi import APIRouter, HTTPException, status
from app.schemas.generation import GenerationRequest, GenerationResponse
from app.services.gemma_service import gemma_service

router = APIRouter()


@router.post(
    "/generate",
    response_model=GenerationResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate text using Gemma",
)
async def generate_text(request: GenerationRequest) -> GenerationResponse:
    try:
        text, model_used = await gemma_service.generate_text(
            prompt=request.prompt,
            model=request.model,
        )
        return GenerationResponse(response=text, model_used=model_used)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gemma inference error: {str(exc)}",
        ) from exc