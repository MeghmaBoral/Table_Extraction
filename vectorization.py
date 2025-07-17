from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import faiss
import numpy as np

corpus_chunks = [
    "Company made a profit of $4.5 million in 2022.",
    "Revenue grew by 8% compared to the previous year.",
    "The balance sheet shows an increase in current assets.",
    "Net loss was recorded in Q1 but recovered in Q2.",
    "Financial tables list quarterly performance in detail."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
corpus_embeddings = model.encode(corpus_chunks)

dimension = corpus_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(corpus_embeddings))

def query_corpus(user_query, top_k=3):
    query_embedding = model.encode([user_query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [corpus_chunks[i] for i in indices[0]]

if __name__ == "__main__":
    query = "What is the company's revenue growth?"
    print("User Query:", query)
    results = query_corpus(query)
    print("\nTop Matches:")
    for r in results:
        print("-", r)
