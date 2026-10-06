from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Prompt text to send to Gemma")
    model: str | None = Field(
        default="gemma-4-26b-a4b-it",
        description="Gemma model override. Defaults to system setting if omitted."
    )


class GenerationResponse(BaseModel):
    response: str
    model_used: str