from pydantic import BaseModel


class ICDRecommendation(BaseModel):
    code: str
    description: str
    confidence: int


class ICDResponse(BaseModel):
    assessment: str
    normalized_diagnoses: list[str]
    recommendations: list[ICDRecommendation]