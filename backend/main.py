from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Text-to-Video Agent Backend")

class VideoRequest(BaseModel):
    prompt: str
    style: str

@app.post("/generate-video")
def generate_video(data: VideoRequest):
    """
    Demo backend endpoint.

    In production, this endpoint connects to GPU-based
    text-to-video models (e.g., Kling, Zeroscope).
    """
    return {
        "status": "demo",
        "prompt": data.prompt,
        "style": data.style,
        "message": "Video generation disabled in demo mode."
    }
