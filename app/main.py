
from fastapi import FastAPI, UploadFile, File
from app.rag import handle_text_query
from app.image_search import handle_image_query
from app.audio_search import handle_audio_query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GemSearch API is live"}

@app.post("/search_text")
def search_text(query: str):
    return handle_text_query(query)

@app.post("/search_image")
def search_image(file: UploadFile = File(...)):
    return handle_image_query(file)

@app.post("/search_audio")
def search_audio(file: UploadFile = File(...)):
    return handle_audio_query(file)
