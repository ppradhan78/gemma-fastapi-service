from google import genai
from app.core.config import settings


class GemmaService:
    def __init__(self) -> None:
        # Client reuses underlying connection pools across requests
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    async def generate_text(self, prompt: str, model: str | None = None) -> tuple[str, str]:
        selected_model = model or settings.DEFAULT_GEMMA_MODEL
        
        response = await self.client.aio.models.generate_content(
            model=selected_model,
            contents=prompt,
        )
        return response.text, selected_model


gemma_service = GemmaService()