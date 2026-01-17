# Text-to-Video AI Agent

## Overview
This project is a Text-to-Video AI Agent that accepts a text prompt and a selectable style (cinematic, anime, realistic) and demonstrates how short videos can be generated from text using an AI-powered pipeline.

The goal of this project is to showcase system design, prompt handling, and deployment of an AI product in a real-world setting.

---

## Features
- Accepts text prompts from the user
- Supports multiple styles (cinematic, anime, realistic)
- Interactive web interface
- Deployed and publicly accessible demo
- Scalable architecture ready for production models

---

## Tech Stack
- **Frontend:** Gradio (Hugging Face Spaces)
- **Backend:** FastAPI (API architecture design)
- **Deployment:** Hugging Face Spaces
- **Language:** Python

---

## Architecture
The system follows a modular architecture:

User  
→ Web Interface (Gradio)  
→ API Layer (FastAPI)  
→ Video Generation Model (Production)

In the current demo, the video generation step is simulated to demonstrate the complete pipeline.

---

## Deployment
The project is deployed using Hugging Face Spaces.

🔗 **Live Demo:**  
https://huggingface.co/spaces/MananAgral/text-to-video-agent

---

## API Design (Backend)
The backend is designed using FastAPI and exposes a `/generate-video` endpoint that accepts:
- `prompt`: text description of the scene
- `style`: visual style of the video

This backend represents the production-ready interface for integrating GPU-based video generation models.

---

## Limitations & Future Work
Due to GPU and cost limitations in the evaluation environment, the deployed demo demonstrates the complete text-to-video pipeline without executing GPU-intensive video generation.

In a production environment, this system can be extended by:
- Integrating GPU-based text-to-video models (e.g., Kling, Zeroscope)
- Generating real video outputs
- Adding controls such as duration, camera motion, and transitions
- Improving video realism and smooth motion

---

## Author
Manan Agrawal
