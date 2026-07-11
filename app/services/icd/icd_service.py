import json
import re
from pathlib import Path
from uuid import UUID

from ollama import chat
from sqlalchemy.orm import Session

from app.repositories.icd_repository import ICDRepository
from app.repositories.soap_repository import SOAPRepository


class ICDService:
    """
    Generates ICD-10 recommendations from the SOAP assessment.
    """

    def __init__(self, db: Session):
        self.soap_repository = SOAPRepository(db)
        self.icd_repository = ICDRepository()

    def recommend(self, audio_id: UUID):

        transcript = self.soap_repository.get_transcript_by_audio(audio_id)

        if transcript is None:
            raise ValueError("Transcript not found.")

        if transcript.soap_note is None:
            raise ValueError("SOAP note not found.")

        assessment = transcript.soap_note.soap_json.get(
            "assessment",
            "",
        )

        prompt = (
            Path("app/prompts/icd_prompt.txt")
            .read_text(encoding="utf-8")
            .replace(
                "{{ASSESSMENT}}",
                assessment,
            )
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

        # Remove markdown fences
        if response_text.startswith("```"):
            response_text = "\n".join(
                line
                for line in response_text.splitlines()
                if not line.startswith("```")
            )

        match = re.search(r"\{[\s\S]*\}", response_text)

        if not match:
            raise ValueError(
                f"No JSON found in Ollama response:\n\n{response_text}"
            )

        json_text = match.group()

        try:
            primary_diagnosis = json.loads(json_text)[
                "primary_diagnosis"
            ]
        except Exception:
            primary_diagnosis = assessment

        recommendations = self.icd_repository.search(
            diagnosis=primary_diagnosis,
            limit=5,
        )

        return {
            "assessment": assessment,
            "normalized_diagnoses": [primary_diagnosis],
            "recommendations": recommendations,
        }