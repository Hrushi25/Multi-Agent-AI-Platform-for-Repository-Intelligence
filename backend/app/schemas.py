from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    github_url: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str

class UploadResponse(BaseModel):
    status: str
    filename: str
    chunks_created: int
