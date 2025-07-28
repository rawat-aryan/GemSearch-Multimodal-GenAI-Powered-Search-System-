
# import whisper

# model = whisper.load_model("base")

# def handle_audio_query(file):
#     with open("temp_audio.wav", "wb") as f:
#         f.write(file.file.read())
#     result = model.transcribe("temp_audio.wav")
#     return {"transcription": result["text"]}
import whisper
from tempfile import NamedTemporaryFile
from app.search_text import handle_text_query

# Load Whisper model (base for speed)
asr_model = whisper.load_model("base")

async def handle_audio_query(file):
    try:
        # Save uploaded audio to a temporary file
        with NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(await file.read())
            temp_audio_path = temp_audio.name

        # Transcribe audio
        result = asr_model.transcribe(temp_audio_path)
        transcript = result["text"]

        print("🎤 Transcript:", transcript)

        # Reuse text search
        return {
            "transcript": transcript,
            "search": handle_text_query(transcript)
        }

    except Exception as e:
        return {"error": str(e)}
