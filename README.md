# Offline YouTube Video Summarizer  
### FastAPI + Whisper + BART + Docker (Fully Offline AI Pipeline)

This project is a fully offline system that:

1. Accepts a **YouTube video URL**
2. Downloads the video's **audio locally**
3. Transcribes the speech using **Whisper (offline)**
4. Summarizes the transcript using **BART Large CNN (offline)**
5. Displays a clean summary through a simple **web interface**

No cloud APIs are used — **all AI runs locally inside Docker**.

---

## 🚀 Features

- Offline **speech-to-text** using Whisper
- Offline **abstractive summarization** using BART
- FastAPI backend with REST API
- Simple HTML/CSS/JS frontend
- Dockerized container for clean deployment
- Chunking system to handle long transcripts
- Robust audio downloading using yt-dlp
- Local model storage under `models/`

---

## 📁 Project Structure

youtube-summarizer/
│ .dockerignore
│ Dockerfile
│ requirements.txt
│ README.md
│
├── app/
│ ├── main.py # FastAPI main app
│ ├── downloader.py # Downloads YouTube audio
│ ├── transcriber.py # Whisper transcription
│ ├── summarizer.py # BART summarizer
│ ├── chunker.py # Splits text into chunks
│ ├── utils.py # Helper functions
│ └── downloads/ # Audio files saved at runtime
│
├── frontend/
│ ├── index.html # Main UI
│ ├── style.css # CSS styling
│ └── app.js # Handles API requests
│
└── models/
└── summarizer/ # BART large model files (1.6GB)

🧠 System Design
1. Audio Downloading
Uses yt-dlp

Uses FFmpeg for audio extraction

Saved at /app/downloads/<id>.mp3

2. Speech-to-Text
Model: Whisper Small

Justification:

Accurate for general speech

Runs well on CPU

Fully offline

3. Summarization
Model: facebook/bart-large-cnn

Justification:

High-quality abstractive summaries

Works offline when pre-downloaded

Balanced accuracy/speed

4. Chunking
Long transcripts exceed model context length → chunking ensures stable summarization.

🔧 Model Setup
The summarizer model must be pre-downloaded into:

models/summarizer/
This folder contains:

pytorch_model.bin

config.json

tokenizer.json

merges.txt

vocab.json

These files are loaded offline by Transformers.

🧩 Error Handling
This system handles:

Invalid YouTube URLs

Audio extraction failures

Missing models

Whisper transcription errors

Long video transcripts

Logs appear in Docker console for debugging.

🧪 Challenges Faced
1. Whisper failing due to deleted audio files
Solved by using yt-dlp postprocessor_hooks to capture the final audio path.

2. Docker static file issues
Fixed by serving /frontend using FastAPI StaticFiles.

3. Model download size
Handled by storing summarizer model under /models/ and mounting it into Docker.

📹 Demo Video
Include a short demo screen recording in your submission.

