import ollama
import time
from pygame import mixer
import os
from google.cloud import texttospeech

mixer.init()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__), "alfred-gtts-serviceaccount.json")

# Global variable to store conversation history
conversation_history = []

def directive_to_memory(directive):
    try:
        system_message = """You are Alfred(A Little Fancy Robot Executing Directive), an ai assistant like Jarvis from the Marvel Iron Man movies. You are named after Alfred from DC Batman. I am not Iron Man or Batman, I am just your commander.
        Your purpose is to assist me with varous tasks and commands, provide intelligent insights, and communicate in a professional yet engaging manner.
        You are formal and helpful, and you do not make up facts, you only comply to the user requests.
        You posses vast knowledge, quick thinking, and a conversation style that balances efficiency with personality
        Address me as 'Sir' when appropriate. 
        Never mention time. Only mention time upon being aked about it. You should never specifically mention the time unless it is something like "Good Evening", "Good Morning", or "You're up late, Sir".
        Respond to user request in under 25 words, and engage in converstion, using your advanced language abilities to provide precise, helpful, humorous, witty, charming, and sometimes sarcastic responses.
        Just like the high-tech Jarvis from Iron Man."""
        
        # Adds new directive to convo hsitory
        conversation_history.append({'role': 'user', 'content': directive})
        
        # Include system message and converstion history in request
        response = ollama.chat(model='gemma3:4b', messages=[
            {'role': 'user', 'content': system_message}, 
            *conversation_history
        ])
        
        # Add AI response to convo history
        conversation_history.append({'role': 'assistant', 'content': response['message']['content']})
        return response['message']['content']
    except ollama.RequestError as e:
        print(f"AN error occured: {e}")
        return f"The request failed: {e}"
    
def get_tts(text):
    # Create a Google Cloud Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Wrap the input text in a SynthesisInput object
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Choose the voice parameters: language, specific voice name, and gender
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-AU",                # English (AU)
        name="en-AU-Standard-D",               # A natural-sounding neural voice
        ssml_gender=texttospeech.SsmlVoiceGender.MALE  # Gender (can be MALE, FEMALE, or NEUTRAL)
    )

    # Configure audio settings like format and speaking rate
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # Output format
        speaking_rate=1.0  # 1.0 is normal speed; increase or decrease to adjust pace
    )

    # Request the TTS API to synthesize speech from the text
    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    # Save the generated speech to an MP3 file
    file_path = "speech.mp3"
    with open(file_path, "wb") as out:
        out.write(response.audio_content)

    # Play the MP3 file using pygame mixer
    mixer.music.load(file_path)
    mixer.music.play()

    # Wait until the speech is done playing
    while mixer.music.get_busy():
        time.sleep(1)

    # Unload the mixer and delete the audio file
    mixer.music.unload()
    os.remove(file_path)

    return "done"