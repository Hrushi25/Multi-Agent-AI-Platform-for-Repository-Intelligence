from typing import List
import numpy as np
from app.rag.store import DocumentChunk, get_all_chunks
from app.rag.embeddings import embed_text

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def semantic_search(query: str, top_k: int = 5) -> List[DocumentChunk]:
    query_embedding = embed_text(query)
    scored_chunks = []

    for chunk in get_all_chunks():
        score = cosine_similarity(query_embedding, chunk.embedding)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return [chunk for _, chunk in scored_chunks[:top_k]]
