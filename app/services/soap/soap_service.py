from pathlib import Path
from uuid import UUID

from google import genai
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.models.soap_note import SOAPNote
from app.repositories.soap_repository import SOAPRepository


class SOAPService:

    def __init__(self, db: Session):
        self.repository = SOAPRepository(db)
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate(self, audio_id: UUID) -> SOAPNote:

        transcript = self.repository.get_transcript_by_audio(audio_id)

        if transcript is None:
            raise ValueError("Transcript not found.")

        prompt = Path(
            "app/prompts/soap_prompt.txt"
        ).read_text()

        prompt = prompt.replace(
            "{{TRANSCRIPT}}",
            transcript.transcript,
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        soap_note = SOAPNote(
            transcript_id=transcript.id,
            soap_json=response.text,
        )

        return self.repository.create(soap_note)