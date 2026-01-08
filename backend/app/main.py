from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ChatRequest, ChatResponse, UploadResponse
from app.rag.ingest import chunk_text
from app.rag.store import add_chunks
from app.agents.retriever import RetrieverAgent
from app.agents.answer import AnswerAgent
from app.tools.github_mcp import fetch_repo_files
from app.rag.ingest import chunk_text
from app.rag.store import add_chunks



app = FastAPI(title="CodeChat-Lite")
retriever_agent = RetrieverAgent()
answer_agent = AnswerAgent()


# CORS (keep permissive for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    content_bytes = await file.read()

    try:
        content = content_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return {
            "status": "error",
            "filename": file.filename,
            "chunks_created": 0
        }

    chunks = chunk_text(
        text=content,
        source=file.filename
    )

    add_chunks(chunks)

    return {
        "status": "success",
        "filename": file.filename,
        "chunks_created": len(chunks)
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if request.github_url:
        files = fetch_repo_files(request.github_url)

        for path, content in files:
            chunks = chunk_text(
                text=content,
                source=f"github:{path}"
            )
            add_chunks(chunks)
    context = retriever_agent.run(request.message)

    answer = answer_agent.run(
        question=request.message,
        context=context
    )

    return {
        "answer": answer
    }
