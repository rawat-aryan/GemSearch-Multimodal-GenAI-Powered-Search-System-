
from sentence_transformers import SentenceTransformer, util
import faiss, json

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)

docs = ["Gemini is Google's LLM.", "CLIP is for image embeddings.", "Whisper transcribes audio."]
doc_embeddings = model.encode(docs)
index.add(doc_embeddings)

def handle_text_query(query):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k=3)
    results = [docs[i] for i in I[0]]
    return {"query": query, "top_results": results}
