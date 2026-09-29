from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.genai.errors import ClientError
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.post("/generate")
def generate_document(request: DocumentRequest):

    generator = GeminiDocumentGenerator()

    try:
        document = generator.generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates
        )

        return {
            "document": document
        }

    except ClientError as e:

        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please try again after the quota resets."
            )

        raise HTTPException(
            status_code=500,
            detail="An error occurred while generating the document."
        )