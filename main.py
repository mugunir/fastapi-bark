from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from bark import generate_audio, SAMPLE_RATE
import soundfile as sf
import os

app = FastAPI()

@app.post("/generate-audio/")
async def generate_audio_from_text(text: str = Form(...)):
    # Generate the audio using Bark TTS
    audio_array = generate_audio(text)
    
    # Save the audio to a file
    output_file = "generated_hindi_output.wav"
    sf.write(output_file, audio_array, SAMPLE_RATE)
    
    # Return the audio file as a response
    return FileResponse(output_file, media_type='audio/wav', filename="output.wav")

@app.get("/")
async def main():
    content = """
    <form action="/generate-audio/" method="post">
        <input type="text" name="text" placeholder="Enter Hindi text">
        <button type="submit">Submit</button>
    </form>
    """
    return content
