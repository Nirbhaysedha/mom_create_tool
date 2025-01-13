import streamlit as st
from PIL import Image
import os
import time
from s2tdepl import main
from mom import MOM
from utils import delr



logo_path = "/Users/nirbhaysedha/Desktop/S2T/KP.jpeg"  # Replace with the actual path to the variable 'image'
kpmg_logo = Image.open(logo_path)

# App Configuration
st.set_page_config(
    page_title="KPMG Digital Trust - Cyber Assurance",
    page_icon=kpmg_logo,
    layout="centered",  # Ensure optimal layout for all screen sizes
)

# Custom CSS for Styling and Responsiveness
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    .main-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    .title {
        font-size: calc(2rem + 1vw);
        color: #00274d;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: calc(1rem + 0.5vw);
        color: #666666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .upload-box {
        border: 2px dashed #ccc;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        background-color: #f9f9f9;
    }
    .footer {
        font-size: 0.9rem;
        color: #999999;
        text-align: center;
        margin-top: 3rem;
    }
    .stButton > button {
        font-size: 1rem;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Container
with st.container():
    
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    # Branding Section
    st.image(kpmg_logo, width=200)  # Dynamically adjust logo size
    st.markdown("<div class='title'>KPMG Digital Trust - Cyber Assurance</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Enhancing trust in a digital world. Upload your audio files and let us take care of the rest!</div>",
        unsafe_allow_html=True,
    )

    # File Upload Section
    st.markdown("## Upload Your Audio File")
    st.markdown("<div class='upload-box'>Drag and drop your MP3 or MP4 file here.</div>", unsafe_allow_html=True)
    delr()
    uploaded_file = st.file_uploader("Supported Formats: MP3, MP4", type=["mp3", "mp4"])
    if uploaded_file:
        current_dir = os.getcwd()
        save_path = os.path.join(current_dir, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())


        # Process and Create Output Files
        st.markdown("### Processing Your File...")
        with st.spinner("Performing operations, please wait..."):
        
            main(save_path)
            MOM('/Users/nirbhaysedha/Desktop/S2T/transcription.txt')

            # Output files
            output_file_1 = "/Users/nirbhaysedha/Desktop/S2T/transcription.txt"
            output_file_2 = "/Users/nirbhaysedha/Desktop/S2T/MoM.txt"
        # Download Buttons
        col1, col2 = st.columns([1, 1])  # Balanced columns for responsive design
        with col1:
            st.download_button(
                label="Download Output File 1",
                data=open(output_file_1, "r").read(),
                file_name=output_file_1,
                mime="text/plain",
            )
        with col2:
            st.download_button(
                label="Download Output File 2",
                data=open(output_file_2, "r").read(),
                file_name=output_file_2,
                mime="text/plain",
            )

    # Footer Section
    st.markdown(
        "<div class='footer'>© 2025 KPMG Digital Trust - Cyber Assurance Team</div>",
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)
