# AI Video Assistant 🎥🤖

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://ai-video-assistant-7klu.onrender.com/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/aditya654685/AI-Video-Assistant)
[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

An AI-powered video meeting assistant that ingests YouTube links or uploaded recordings, extracts and normalizes audio, transcribes speech with multilingual support (English & Hinglish), generates structured meeting summaries and action items, and lets you chat with your video content using a RAG (Retrieval-Augmented Generation) pipeline.

🔗 **Live Application:** [https://ai-video-assistant-7klu.onrender.com/](https://ai-video-assistant-7klu.onrender.com/)

---

## Key Features ✨

- **Multi-Source Ingestion**: Process YouTube URLs directly or upload local video/audio files (`.mp4`, `.mov`, `.mkv`, `.mp3`, `.wav`, etc.).
- **Smart Audio Processing**: Automatic audio extraction, 16kHz mono normalization, and size-controlled chunking (guaranteed under API upload limits).
- **Speech-to-Text Transcription**: Accurate transcription powered by `whisper-large-v3-turbo` via Euri API with automated Hinglish-to-English translation.
- **Automated Insights**:
  - 📌 Concise, professional meeting title
  - 📋 Comprehensive executive summary
  - ✅ Action items with assigned owners and deadlines
  - 🔑 Key decisions made
  - ❓ Open questions and follow-ups
- **Interactive RAG Q&A Chat**: Query your meeting or video using ChromaDB vector store and LangChain retrieval chains.
- **Export Reports**: One-click download of structured Markdown reports and raw transcripts.

---

## Project Structure 📁

```text
├── core/
│   ├── extractor.py       # Action items, decisions, questions extraction
│   ├── rag_engine.py      # Vector retrieval & RAG Q&A chain
│   ├── summarize.py       # Title generation & summarization
│   ├── transcriber.py     # Whisper transcription & translation engine
│   └── vector_store.py    # ChromaDB vector store management
├── utils/
│   └── audio_processor.py # YouTube download, 16kHz conversion & chunking
├── app.py                 # Streamlit web application
├── main.py                # Command-line interface (CLI)
├── Dockerfile             # Docker container definition with FFmpeg
├── render.yaml            # Render Blueprint for automated deployment
├── requirements.txt       # Python dependencies
└── .env.example           # Example environment variables template
```

---

## Getting Started Locally 🚀

### 1. Clone the Repository
```bash
git clone https://github.com/aditya654685/AI-Video-Assistant.git
cd AI-Video-Assistant
```

### 2. Set Up a Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note**: Audio processing uses `ffmpeg`. Ensure FFmpeg is installed on your system or available in your environment.

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and insert your API key:
```bash
cp .env.example .env
```
Inside `.env`:
```env
EURI_API_KEY="your-euri-api-key-here"
```

### 5. Run the Application

**Streamlit Web Interface (Recommended):**
```bash
streamlit run app.py
```

**CLI Pipeline:**
```bash
python main.py
```

---

## Deployment on Render ☁️

This project is fully containerized and configured for [Render](https://render.com/).

### Deployment Steps:
1. Fork or push this repository to GitHub.
2. Sign in to [Render Dashboard](https://dashboard.render.com/) and click **New + > Web Service**.
3. Connect your **`AI-Video-Assistant`** repository.
4. Set the following configuration:
   - **Environment / Runtime**: `Docker`
   - **Branch**: `main`
   - **Plan**: `Free`
5. Under **Environment Variables**, add:
   - `EURI_API_KEY`: `your-euri-api-key`
6. Click **Deploy Web Service**.

Render will automatically build the Docker container (with system `ffmpeg`), install dependencies, and launch Streamlit on your custom `.onrender.com` URL.

---

## Environment Variables

| Variable | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `EURI_API_KEY` | **Yes** | — | Euri API key for Whisper and LLM completion |
| `EURI_STT_MODEL` | No | `openai/whisper-large-v3-turbo` | Speech-to-text model identifier |
| `EURI_CHAT_MODEL` | No | `gpt-4.1-mini` | Chat and summarization model identifier |

---

## License

This project is licensed under the [MIT License](LICENSE).
