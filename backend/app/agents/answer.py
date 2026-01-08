from typing import List, Dict
from app.llm.client import GeminiClient

SYSTEM_INSTRUCTIONS = """
You are an AI assistant that answers questions using ONLY the provided context.

Rules:
- Use only the given context.
- You may summarize or describe the repository based on what the context says.
- Do NOT assume features or technologies not mentioned.
- If the context is insufficient even for a summary, say:
  "I don't have enough information in the provided files to answer this."
- Be clear and concise.
"""

class AnswerAgent:
    def __init__(self):
        self.llm = GeminiClient()

    def run(self, question: str, context: List[Dict]) -> str:
        if not context:
            return "I don't have enough information in the provided files to answer this."

        formatted_context = "\n\n".join(
            f"Source: {c['source']}\n{c['content']}"
            for c in context
        )

        prompt = f"""
{SYSTEM_INSTRUCTIONS}

Context:
{formatted_context}

Question:
{question}

Answer:
"""

        return self.llm.generate(prompt)
