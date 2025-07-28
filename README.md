# 🔍 GemSearch: GenAI-Powered Multimodal Search System

GemSearch is a **multimodal semantic search engine** that allows you to search using **text**, **image**, or **audio** inputs. It uses state-of-the-art open-source models for embedding and retrieval, and integrates them into a unified FastAPI backend with a Streamlit frontend.

---

## 🚀 Features

- ✅ **Text Search** via Sentence Transformers
- 🖼️ **Image Search** using OpenAI CLIP embeddings
- 🔊 **Audio Search** using Whisper transcription + text embedding
- 🧠 Ready to integrate **Gemini Pro/Vision** APIs for GenAI workflows
- 📦 Lightweight, modular structure with FastAPI & Streamlit
- 🌐 Run locally or deploy to Codespaces, Docker, or Cloud

---

## 🗂️ Project Structure

GemSearch/
│
├── app/ # Core backend logic

│ ├── main.py # FastAPI entrypoint

│ ├── search_text.py # SentenceTransformer-based text search

│ ├── search_image.py # CLIP-based image search

│ ├── search_audio.py # Whisper-based audio transcription + search

│
├── ui/
│ └── streamlit_app.py # Multimodal search interface
│
├── models/ # (Optional) Store downloaded model weights
├── data/ # (Optional) Sample input files
├── requirements.txt # Python dependencies
└── README.md # Project overview and guide


---

## 🧠 Models Used

| Modality | Task                     | Model                                  |
|----------|--------------------------|----------------------------------------|
| Text     | Semantic Search          | `sentence-transformers/all-MiniLM-L6-v2` |
| Image    | Embedding + Caption Match| `OpenAI CLIP (ViT-B/32)`               |
| Audio    | Speech to Text           | `openai/whisper (base)`                |
| Optional | GenAI Answering          | `Gemini Pro / Gemini Vision` API       |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/GemSearch.git
cd GemSearch


2. Create Virtual Environment

python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt


4. Fix CLIP Module (If needed)
If clip.load(...) throws an error:

pip uninstall clip -y
pip install git+https://github.com/openai/CLIP.git


▶️ Running the Project
Start the FastAPI Backend

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

By default, the API runs at:
http://localhost:8000/docs → FastAPI Swagger UI
http://localhost:8000/search_text → POST endpoint for queries

Start the Streamlit Frontend
Open a new terminal and run:

streamlit run ui/streamlit_app.py
This will open the web app at:
http://localhost:8501/



🔎 How It Works
Text Search
Takes user query → embeds with SentenceTransformer

Computes cosine similarity with sample corpus embeddings

Returns top matching entries

Image Search
Upload image → CLIP extracts visual embedding

Compared with a set of caption embeddings

Returns top-matching captions

Audio Search
Upload audio → Whisper transcribes to text

The transcript is processed by text search logic

🧪 Demo Inputs
You can test with:

dog (text)

Any photo (e.g., landscape, dog, computer)

Voice audio saying "A dog playing in the park"

🔧 Optional: Gemini API Integration
To use Gemini Pro or Vision:

Install google-generativeai

Configure with your API Key

Wrap text/image/audio content via Gemini model prompt
(Ask me for code snippets if you'd like this added.)

📌 Future Improvements
Add Gemini Pro response fallback

Store indexed corpora in vector DB (e.g., FAISS, ChromaDB)

Streamlined Docker deployment

Upload video and extract multimodal content

🧑‍💻 Author
Aryan Rawat
ML Engineer | CV & MLOps | FastAPI | GCP
