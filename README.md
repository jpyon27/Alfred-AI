# Alfred - Voice AI Assistant

**Alfred** is a real-time, voice-activated AI assistant inspired by Jarvis from Iron Man. It uses speech recognition, language modeling, and text-to-speech to respond intelligently and conversationally to user commands.

---

## Requirements

- Python < 3.12
- [Ollama](https://ollama.com) (with a compatible model running like `gemma:2b` or `gemma:1b`)
- Google Cloud Text-to-Speech credentials JSON

---

## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/jpyon27/alfred-voice-ai.git
```

2. **Install Dependencies:**

```bash
pip install pygame
pip install torch
pip install google-cloud-texttospeech
pip install RealtimeSTT
pip install ollama
```

3. **Set Up Google Cloud TTS:**

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Text-to-Speech API**
- Create a **Service Account**, download the JSON key
- Place the key in the root directory (same location as `assistant.py`)

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__), "your_credentials_file.json")
```

---

## Usage

Start the assistant with:

```bash
python alfred.py
```

Speak aloud. Once you say **"Alfred"**, it will respond and carry out your command.

---

## Example Use Cases

- Ask questions
- Expand with custom commands or smart home integration

---

## Credits

- [RealtimeSTT](https://github.com/SYSTRAN/RealtimeSTT)
- [Ollama](https://ollama.com/)
- [Google Cloud TTS](https://cloud.google.com/text-to-speech)
- [pygame](https://www.pygame.org/)
