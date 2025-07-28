#!/bin/bash

echo "🔁 Activating virtual environment..."
if [ ! -d "venv" ]; then
    echo "⚙️ Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check for Whisper FFmpeg dependency (Linux/Debian)
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️ ffmpeg not found. Installing (Ubuntu/Debian only)..."
    sudo apt update && sudo apt install ffmpeg -y
fi

# Load Whisper model once
echo "🔊 Preloading Whisper model (base)..."
python3 -c "import whisper; whisper.load_model('base')"

# Load Gemini config
if [ -f .env ]; then
    echo "🔐 .env file detected. Gemini API key will be used."
else
    echo "❌ .env file not found. Please create one with GEMINI_API_KEY=..."
    exit 1
fi

# Start FastAPI backend
echo "🚀 Starting FastAPI backend..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
