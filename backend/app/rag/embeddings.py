from sentence_transformers import SentenceTransformer

# Lightweight, fast, very popular model
MODEL_NAME = "all-MiniLM-L6-v2"

_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer(MODEL_NAME)
    return _embedding_model

def embed_text(text: str):
    model = get_embedding_model()
    return model.encode(text)
