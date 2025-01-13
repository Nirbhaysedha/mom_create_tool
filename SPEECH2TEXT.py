from pydub import AudioSegment
import whisper
import streamlit as st
import os
from llm import AI

def inputmp3():
    st.markdown(
        """
        <h1 style='color:lightblue; font-weight: bold;'>KPMG Internal Audits 📊</h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h3 style='color: lightblue; font-weight: bold;'>🔒 DT-Cyber Assurance</h3>
        """,
        unsafe_allow_html=True
    )
    st.title("Upload client audio 🎙️")
    uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3","mp4"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        with open(f"uploaded_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.info(f"File saved as 'uploaded_{uploaded_file.name}' in the current directory.")
    else:
        st.info("Please upload an MP3 file to continue.")
    return uploaded_file

inpu=inputmp3()

def chunk_mp3(input_mp3, chunk_duration=30):
    try:
        sound = AudioSegment.from_mp3(input_mp3)
        chunk_duration_ms = chunk_duration * 1000  # Convert seconds to milliseconds
        output_dir = "chunks"
        os.makedirs(output_dir, exist_ok=True)
        total_duration_ms = len(sound)
        num_chunks = (total_duration_ms + chunk_duration_ms - 1) // chunk_duration_ms  # Ceiling division
        for i in range(num_chunks):
            start_time = i * chunk_duration_ms
            end_time = min(start_time + chunk_duration_ms, total_duration_ms)
            chunk = sound[start_time:end_time]
            chunk_name = os.path.join(output_dir, f"chunk_{i+1}.mp3")
            chunk.export(chunk_name, format="mp3")
            print(f"Saved {chunk_name}") 
        print(f"All chunks saved in '{output_dir}' directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

chunk_mp3(inpu)

def inference():
    model = whisper.load_model("base")
    for root, _, files in os.walk('chunks'):
            for file in files:
                file_path = os.path.join(root, file)
                audio = whisper.load_audio(file_path)
                audio = whisper.pad_or_trim(audio)
                mel = whisper.log_mel_spectrogram(audio).to(model.device)
                _, probs = model.detect_language(mel)
                print(f"Detected language: {max(probs, key=probs.get)}")
                options = whisper.DecodingOptions()
                result = whisper.decode(model, mel, options)
                a=result.text
                try:
                    with open('data.txt', 'a') as file:
                        file.write(a)
                        file.write("\n") 
                except Exception as e:
                    print(f"An error occurred: {e}")

inference()



