from utility.retriever import KnowledgeRetriever


retriever = KnowledgeRetriever(
    "data/knowledge_base.json"
)

ticket = "My VPN is not connecting"

results = retriever.search(ticket)

for result in results:
    print(result)