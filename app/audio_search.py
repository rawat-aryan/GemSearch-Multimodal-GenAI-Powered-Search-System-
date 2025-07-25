
import whisper

model = whisper.load_model("base")

def handle_audio_query(file):
    with open("temp_audio.wav", "wb") as f:
        f.write(file.file.read())
    result = model.transcribe("temp_audio.wav")
    return {"transcription": result["text"]}
