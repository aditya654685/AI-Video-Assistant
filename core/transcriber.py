import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# One client, one key: used for both Whisper (speech-to-text) and GPT (translation)
client = OpenAI(
    api_key=os.environ["EURI_API_KEY"],
    base_url="https://api.euron.one/api/v1/euri",
)

STT_MODEL = os.getenv("EURI_STT_MODEL", "openai/whisper-large-v3-turbo")
# Set this to the same GPT model name you already use elsewhere in the project
CHAT_MODEL = os.getenv("EURI_CHAT_MODEL", "gpt-4.1-mini")

# Romanised Hinglish prompt nudges Whisper toward Latin script instead of Devanagari
HINGLISH_PROMPT = (
    "Haan, toh aaj ki meeting mein hum project ke baare mein baat karenge. "
    "Okay, let's discuss the next steps."
)


def transcribe_chunk(chunk_path: str, language: str = "english") -> str:
    """
    Transcribe one chunk with whisper-large-v3-turbo via Euri.
    - english  -> language pinned to 'en'
    - hinglish -> auto-detect, steered toward romanised Hinglish
    """
    kwargs = {"model": STT_MODEL}

    if language.lower() == "english":
        kwargs["language"] = "en"
    else:
        kwargs["prompt"] = HINGLISH_PROMPT

    with open(chunk_path, "rb") as f:
        resp = client.audio.transcriptions.create(file=f, **kwargs)

    return resp.text.strip()


def translate_to_english(text: str) -> str:
    """Convert a Hindi/Hinglish transcript to clean English using the GPT model."""
    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "Translate the following Hindi/Hinglish transcript into natural English. "
                    "Keep names, numbers and technical terms unchanged. "
                    "Return only the translation."
                ),
            },
            {"role": "user", "content": text},
        ],
    )
    return resp.choices[0].message.content.strip()


def transcribe_all(chunks: list, language: str = "english", to_english: bool = True) -> str:
    print(f"Using {STT_MODEL} via Euri for transcription.")

    parts = []
    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1}/{len(chunks)}...")
        parts.append(transcribe_chunk(chunk, language=language))

    full_transcript = " ".join(p for p in parts if p)

    if language.lower() == "hinglish" and to_english:
        print("Translating Hinglish transcript to English...")
        full_transcript = translate_to_english(full_transcript)

    print("Transcription complete.")
    return full_transcript