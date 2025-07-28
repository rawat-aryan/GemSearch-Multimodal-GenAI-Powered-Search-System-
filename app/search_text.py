from sentence_transformers import SentenceTransformer, util
import torch

# Sample corpus
corpus = [
    "A dog playing fetch in the park.",
    "An astronaut floating in space.",
    "A guide to deploying FastAPI with Docker.",
    "A lecture on generative AI and transformers.",
]
# Load sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

def handle_text_query(query: str):
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, corpus_embeddings)[0]
    top_k = torch.topk(similarities, k=3)

    results = []
    for idx in top_k.indices:
        results.append({
            "content": corpus[idx],
            "score": round(float(similarities[idx]), 4)
        })

    return {
        "query": query,
        "results": results
    }
