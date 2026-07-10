import json
from pathlib import Path
from uuid import UUID

from ollama import chat
from sqlalchemy.orm import Session

from app.database.models.soap_note import SOAPNote
from app.repositories.soap_repository import SOAPRepository


class SOAPService:
    """
    Generates SOAP notes using a local Ollama model.
    """

    def __init__(self, db: Session):
        self.repository = SOAPRepository(db)

    def generate(self, audio_id: UUID) -> SOAPNote:

        transcript = self.repository.get_transcript_by_audio(audio_id)

        if transcript is None:
            raise ValueError("Transcript not found.")

        prompt = Path(
            "app/prompts/soap_prompt.txt"
        ).read_text(encoding="utf-8")

        prompt = prompt.replace(
            "{{TRANSCRIPT}}",
            transcript.transcript,
        )

        response = chat(
            model="mistral:latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        response_text = response.message.content.strip()

        # Remove markdown code fences if present
        if response_text.startswith("```"):
            lines = response_text.splitlines()
            lines = [line for line in lines if not line.startswith("```")]
            response_text = "\n".join(lines)

        soap_data = json.loads(response_text)

        soap_note = SOAPNote(
            transcript_id=transcript.id,
            soap_json=soap_data,
        )

        return self.repository.create(soap_note)