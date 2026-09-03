ai-voice-bot

Show Image Show Image

A real-time AI voice assistant that listens, thinks, and talks back — built with OpenAI Whisper, Google Gemini, and ElevenLabs.

How It Works

You speak → your voice is recorded and transcribed → sent to Gemini for a response → ElevenLabs converts the response to speech → you hear it back. Runs in a continuous loop.

Mic → Whisper (STT) → Gemini (LLM) → ElevenLabs (TTS) → Speaker Layer Provider Speech-to-Text OpenAI Whisper (local) Language Model Google Gemini 2.0 Flash Text-to-Speech ElevenLabs Audio I/O sounddevice + scipy Quickstart

Clone the repo

bash git clone https://github.com/rushiltandon05-lgtm/ai-voice-bot cd ai-voice-bot

Install dependencies

bash pip install google-genai python-dotenv openai-whisper sounddevice scipy elevenlabs brew install ffmpeg

Add your API keys

Create a storage.env file in the root folder:

GEMINI_API_KEY=your_gemini_key_here ELEVEN_LABS_API_KEY=your_elevenlabs_key_here

Get your keys from:

Gemini: aistudio.google.com ElevenLabs: elevenlabs.io

Run

bash python gemini.py

Speak when the program starts. It will record for 5 seconds, process your voice, and respond out loud. Press Ctrl+C to stop.

Project Structure ai-voice-bot/ ├── gemini.py # Main loop — connects all components ├── recording_sound.py # Mic recording + Whisper transcription ├── storage.env # API keys (not committed to Git) └── .gitignore Built With OpenAI Whisper — local speech recognition Google Gemini API — large language model ElevenLabs — text-to-speech sounddevice — audio recording# ai-voice-bot
