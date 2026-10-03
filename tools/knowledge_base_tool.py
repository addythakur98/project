from utility.retriever import KnowledgeRetriever

retriever = KnowledgeRetriever(
    "data/knowledge_base.json"
)


def search_similar_solution(problem: str):
    results = retriever.search(problem, top_k=2)

    return results