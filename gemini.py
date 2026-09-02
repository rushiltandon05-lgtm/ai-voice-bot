from google import genai
from dotenv import load_dotenv
from recording_sound import rec_convert


from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os



load_dotenv("storage.env")


elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVEN_LABS_API_KEY"),

)



client = genai.Client()

while True:

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents=rec_convert()
    )

    print(response.text)


    audio = elevenlabs.text_to_speech.convert(
    text = response.text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_v3",
    output_format="mp3_44100_128",
    )


    play(audio)
