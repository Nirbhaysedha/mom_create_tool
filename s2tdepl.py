import os
from pydub import AudioSegment
from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
load_dotenv()
key=os.getenv("key")
def pre():
    API_KEY = key
    os.environ["OPENAI_API_KEY"] = API_KEY
    client = OpenAI(api_key=API_KEY) 
    TEMP_FOLDER = "./temp"
    TRANSCRIPTION_FILE = "./transcription.txt"
    CHUNK_DURATION_MS = 30 * 1000 
    os.makedirs(TEMP_FOLDER, exist_ok=True)
    return CHUNK_DURATION_MS,TRANSCRIPTION_FILE,client,TEMP_FOLDER

def split_audio_into_chunks(audio_file, chunk_duration_ms,TEMP_FOLDER):
    audio = AudioSegment.from_file(audio_file)
    total_chunks = len(audio) // chunk_duration_ms + 1
    chunks = []
    for i in range(total_chunks):
        start_time = i * chunk_duration_ms
        end_time = min((i + 1) * chunk_duration_ms, len(audio))
        chunk = audio[start_time:end_time]
        chunk_path = os.path.join(TEMP_FOLDER, f"chunk_{i + 1}.mp3")
        chunk.export(chunk_path, format="mp3")
        chunks.append(chunk_path)

    print(f"Split audio into {len(chunks)} chunks.")
    return chunks
def transcribe_audio_chunks(chunks,TRANSCRIPTION_FILE,client):
    with open(TRANSCRIPTION_FILE, "w") as transcription_file:
        for i, chunk_path in enumerate(chunks):
            print(f"Transcribing chunk {i + 1}/{len(chunks)}...")
            try:
                with open(chunk_path, "rb") as audio_file:
                    transcription = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file
                    )
                transcription_text = transcription.text
                transcription_file.write(f"Chunk {i + 1}:\n{transcription_text}\n\n")
                print(f"Chunk {i + 1} transcribed successfully.")
            except Exception as e:
                print(f"Error transcribing chunk {i + 1}: {e}")

def main(audio_file):
    CHUNK_DURATION_MS,TRANSCRIPTION_FILE,client,TEMP_FOLDER=pre()
    chunks=split_audio_into_chunks(audio_file, CHUNK_DURATION_MS,TEMP_FOLDER)
    transcribe_audio_chunks(chunks,TRANSCRIPTION_FILE,client)



