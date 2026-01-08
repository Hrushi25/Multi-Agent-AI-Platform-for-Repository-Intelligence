from typing import List
from app.rag.store import DocumentChunk
from app.rag.embeddings import embed_text
import uuid

def chunk_text(
    text: str,
    source: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> List[DocumentChunk]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk_content = text[start:end]

        embedding = embed_text(chunk_content)

        chunks.append(
            DocumentChunk(
                id=str(uuid.uuid4()),
                content=chunk_content,
                source=source,
                embedding=embedding
            )
        )

        start = end - overlap
        if start < 0:
            start = 0

    return chunks
