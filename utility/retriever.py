import json
import numpy as np
from sentence_transformers import SentenceTransformer


class KnowledgeRetriever:

    def __init__(self, knowledge_file):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        with open(knowledge_file, "r") as file:
            self.knowledge_base = json.load(file)

        self.embeddings = self.model.encode(
            [item["problem"] for item in self.knowledge_base]
        )

    def search(self, ticket, top_k=2):

        ticket_embedding = self.model.encode([ticket])[0]

        similarities = np.dot(
            self.embeddings,
            ticket_embedding
        ) / (
            np.linalg.norm(self.embeddings, axis=1)
            * np.linalg.norm(ticket_embedding)
        )

        indices = np.argsort(similarities)[::-1][:top_k]

        return [
            self.knowledge_base[i]
            for i in indices
        ]