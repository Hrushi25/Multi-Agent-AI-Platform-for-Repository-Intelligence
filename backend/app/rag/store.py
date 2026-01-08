from typing import List
from dataclasses import dataclass
import numpy as np

@dataclass
class DocumentChunk:
    id: str
    content: str
    source: str
    embedding: np.ndarray

# Global in-memory store
DOCUMENT_STORE: List[DocumentChunk] = []

def add_chunks(chunks: List[DocumentChunk]):
    DOCUMENT_STORE.extend(chunks)

def get_all_chunks() -> List[DocumentChunk]:
    return DOCUMENT_STORE

def clear_store():
    DOCUMENT_STORE.clear()
