# AI Video Agent 🎥🤖

An AI-powered video processing assistant that extracts audio from videos (YouTube or local files), transcribes speech, generates summaries and key insights, and provides an interactive RAG-based chat interface to query your video contents.

## Features ✨

- **Multi-Source Ingestion**: Process YouTube URLs or local video/audio files.
- **Audio Processing & Chunking**: Automatic audio extraction and chunking for smooth processing.
- **Transcription**: Accurate speech-to-text transcription with multi-language support (English/Hinglish).
- **Insight Extraction**:
  - Automated title generation
  - Comprehensive video summary
  - Action items detection
  - Key decisions & open questions
- **RAG Q&A Chain**: Chat with your meeting or video using a Retrieval-Augmented Generation (RAG) vector store.
- **Interactive UI & CLI**: Run via Streamlit web interface or command line.

## Project Structure 📁

```text
├── core/
│   ├── extractor.py       # Action items, decisions, questions extraction
│   ├── rag_engine.py      # Vector retrieval & RAG QA chain
│   ├── summarize.py       # Title generation & summarization
│   ├── transcriber.py     # Audio transcription engine
│   └── vector_store.py    # Vector store management
├── utils/
│   └── audio_processor.py # YouTube download & audio conversion/chunking
├── app.py                 # Streamlit web application
├── main.py                # Command-line entry point
├── Requirements.txt       # Dependencies
└── .env.example           # Example environment variables
```

## Getting Started 🚀

### 1. Clone the Repository
```bash
git clone <YOUR_REPO_URL>
cd "Video Agent"
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r Requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and provide your API keys:
```bash
cp .env.example .env
```
Add your `EURI_API_KEY` or any required model keys in `.env`.

### 5. Run the Application

**Streamlit Web Interface:**
```bash
streamlit run app.py
```

**CLI Pipeline:**
```bash
python main.py
```

## License
MIT License
