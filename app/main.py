from fastapi import FastAPI
from app.search_text import handle_text_query
from app.search_image import handle_image_query
from app.search_audio import handle_audio_query
from fastapi import UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="GemSearch API")

# -------- TEXT --------
class TextQuery(BaseModel):
    query: str

@app.post("/search_text")
def search_text(data: TextQuery):
    return handle_text_query(data.query)

# -------- IMAGE --------
@app.post("/search_image")
async def search_image(file: UploadFile = File(...)):
    return await handle_image_query(file)

# -------- AUDIO --------
@app.post("/search_audio")
async def search_audio(file: UploadFile = File(...)):
    return await handle_audio_query(file)
