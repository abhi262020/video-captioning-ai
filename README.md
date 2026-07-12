# 🎥 Video Captioning AI

An AI-powered Video Captioning platform that automatically generates descriptive captions and speech transcripts from uploaded videos. The project combines computer vision, automatic speech recognition, and large language models to produce meaningful and accessible video descriptions.

---

## ✨ Features

* 🎬 Upload video files through a modern React interface
* 🖼️ Extract key frames using OpenCV
* 🤖 Generate visual captions with BLIP/CLIP models
* 🎙️ Convert speech to text using Whisper
* 🧠 Enhance captions with Fireworks AI LLM
* 📊 Display confidence score and processing time
* ⚡ FastAPI REST API backend
* ⚛️ React + TypeScript frontend
* 📦 Modular and scalable project architecture

---

## 🏗️ Architecture

```text
                 Video Upload
                      │
                      ▼
              React Frontend
                      │
                      ▼
              FastAPI Backend
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
Frame Extraction                Audio Extraction
   (OpenCV)                        (FFmpeg)
      │                               │
      ▼                               ▼
 BLIP / CLIP                     Whisper ASR
      │                               │
      └───────────────┬───────────────┘
                      ▼
             Fireworks AI LLM
                      │
                      ▼
      Enhanced Caption + Transcript
                      │
                      ▼
                 JSON Response
```

---

## 🛠️ Tech Stack

### Frontend

* React
* TypeScript
* Vite
* CSS

### Backend

* FastAPI
* Python

### AI & Machine Learning

* OpenCV
* Transformers
* BLIP
* CLIP
* Whisper
* Fireworks AI

---

## 📁 Project Structure

```text
video-captioning-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── processed/
│   ├── models_cache/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── types/
│   │   ├── App.tsx
│   │   └── main.tsx
│   │
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/video-captioning-ai.git
cd video-captioning-ai
```

### Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file based on `.env.example`, then start the backend:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

The frontend will be available at:

```
http://localhost:5173
```

---

## 📡 API Endpoints

| Method | Endpoint   | Description                           |
| ------ | ---------- | ------------------------------------- |
| GET    | `/`        | API status                            |
| GET    | `/health`  | Health check                          |
| POST   | `/caption` | Upload a video and generate a caption |

---

## 📋 Example Response

```json
{
  "video_id": "12345678",
  "filename": "sample.mp4",
  "caption": "A person is walking through a park while talking to the camera.",
  "transcript": "Welcome everyone to today's walk in the park.",
  "confidence": 0.92,
  "processing_time": 4.15
}
```

---

## 🗺️ Roadmap

* [x] React frontend
* [x] FastAPI backend
* [x] Video upload
* [x] REST API
* [ ] OpenCV frame extraction
* [ ] Whisper speech transcription
* [ ] BLIP/CLIP caption generation
* [ ] Fireworks AI caption enhancement
* [ ] Multi-language captions
* [ ] Real-time video captioning
* [ ] Docker deployment
* [ ] Cloud deployment

---

## 🤝 Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request to improve the project.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
