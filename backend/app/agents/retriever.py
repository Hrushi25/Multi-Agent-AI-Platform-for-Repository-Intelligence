from typing import List, Dict
from app.rag.search import semantic_search

class RetrieverAgent:
    def run(self, query: str) -> List[Dict]:
        results = semantic_search(query)

        context = []
        for chunk in results:
            context.append({
                "source": chunk.source,
                "content": chunk.content
            })

        return context
