from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.downloader import download_audio
from app.transcriber import transcribe_audio
from app.chunker import chunk_text
from app.summarizer import summarize_chunks

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (CSS, JS)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return FileResponse("frontend/index.html")

@app.post("/process_video")
def process_video(url: str = Form(...)):
    audio_path = download_audio(url)
    transcript = transcribe_audio(audio_path)
    chunks = chunk_text(transcript)
    summary = summarize_chunks(chunks)
    return {"summary": summary}
