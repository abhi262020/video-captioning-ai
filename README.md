# Video Captioning AI

## Features

- Video upload
- Frame extraction
- AI caption generation
- Speech transcription
- LLM caption enhancement


## Architecture

Video
 ↓
OpenCV
 ↓
BLIP/CLIP
 ↓
Whisper
 ↓
Fireworks LLM
 ↓
Caption


## Run Backend

pip install -r requirements.txt

uvicorn app.main:app --reload