# ai-voice-bot

![Python](https://img.shields.io/badge/Python-3.13+-blue) ![License](https://img.shields.io/badge/License-MIT-green)

A real-time AI voice assistant that listens, thinks, and talks back — built with OpenAI Whisper, Google Gemini, and ElevenLabs.

---

## How It Works

You speak → your voice is recorded and transcribed → sent to Gemini for a response → ElevenLabs converts the response to speech → you hear it back. Runs in a continuous loop.

```
Mic → Whisper (STT) → Gemini (LLM) → ElevenLabs (TTS) → Speaker
```

| Layer | Provider |
|---|---|
| Speech-to-Text | OpenAI Whisper (local) |
| Language Model | Google Gemini 2.0 Flash |
| Text-to-Speech | ElevenLabs |
| Audio I/O | sounddevice + scipy |

---

## Quickstart

**1. Clone the repo**

```bash
git clone https://github.com/rushiltandon05-lgtm/ai-voice-bot
cd ai-voice-bot
```

**2. Install dependencies**

```bash
pip install google-genai python-dotenv openai-whisper sounddevice scipy elevenlabs
brew install ffmpeg
```

**3. Add your API keys**

Create a `storage.env` file in the root folder:

```
GEMINI_API_KEY=your_gemini_key_here
ELEVEN_LABS_API_KEY=your_elevenlabs_key_here
```

Get your keys from:
- Gemini: [aistudio.google.com](https://aistudio.google.com)
- ElevenLabs: [elevenlabs.io](https://elevenlabs.io)

**4. Run**

```bash
python gemini.py
```

Speak when the program starts. It records for 5 seconds, processes your voice, and responds out loud. Press `Ctrl+C` to stop.

---

## Project Structure

```
ai-voice-bot/
├── gemini.py            # Main loop — connects all components
├── recording_sound.py   # Mic recording + Whisper transcription
├── storage.env          # API keys (not committed to Git)
└── .gitignore
```

---

## Built With

- [OpenAI Whisper](https://github.com/openai/whisper) — local speech recognition
- [Google Gemini API](https://ai.google.dev/) — large language model
- [ElevenLabs](https://elevenlabs.io/) — text-to-speech
- [sounddevice](https://python-sounddevice.readthedocs.io/) — audio recording
