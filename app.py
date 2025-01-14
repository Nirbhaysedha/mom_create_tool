import streamlit as st
from PIL import Image
import os
import time
from s2tdepl import main
from mom import MOM
from utils import delr



logo_path = "./KP.jpeg"  # Replace with the actual path to the variable 'image'
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
            MOM('./transcription.txt')

            # Output files
            output_file_1 ="./transcription.txt"
            output_file_2 = "./MoM.txt"
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







# from fastapi import FastAPI, UploadFile, Form
# from fastapi.responses import HTMLResponse, StreamingResponse
# from fastapi.staticfiles import StaticFiles
# from io import BytesIO
# from zipfile import ZipFile
# import os
# import shutil
# import uvicorn
# from s2tdepl import main
# from mom import MOM
# from utils import delr

# # Initialize FastAPI app
# app = FastAPI()

# # Paths
# UPLOAD_DIR = "./uploads"
# OUTPUT_DIR = "./outputs"
# LOGO_PATH = "./KP.jpeg"
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Serve static files for logo
# app.mount("/static", StaticFiles(directory=os.path.dirname(LOGO_PATH)), name="static")

# # State to track file readiness
# is_file_ready = False

# # Home route with the HTML interface
# @app.get("/", response_class=HTMLResponse)
# async def home():
#     global is_file_ready
#     download_button = ""
#     if is_file_ready:
#         download_button = """
#             <br>
#             <form action="/download-all" method="get">
#                 <button type="submit" style="font-size: 1rem; padding: 10px 20px;">Download Processed Files</button>
#             </form>
#         """
#     html_content = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>KPMG Digital Trust - Cyber Assurance</title>
#         <style>
#             body {{
#                 font-family: 'Arial', sans-serif;
#                 margin: 0;
#                 padding: 0;
#                 overflow-x: hidden;
#             }}
#             .main-container {{
#                 max-width: 800px;
#                 margin: auto;
#                 padding: 20px;
#             }}
#             .title {{
#                 font-size: calc(2rem + 1vw);
#                 color: #00274d;
#                 text-align: center;
#                 font-weight: bold;
#             }}
#             .subtitle {{
#                 font-size: calc(1rem + 0.5vw);
#                 color: #666666;
#                 text-align: center;
#                 margin-bottom: 2rem;
#             }}
#             .upload-box {{
#                 border: 2px dashed #ccc;
#                 padding: 20px;
#                 border-radius: 10px;
#                 text-align: center;
#                 background-color: #f9f9f9;
#             }}
#             .footer {{
#                 font-size: 0.9rem;
#                 color: #999999;
#                 text-align: center;
#                 margin-top: 3rem;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="main-container">
#             <img src="/static/{os.path.basename(LOGO_PATH)}" alt="KPMG Logo" width="200" />
#             <div class="title">KPMG Digital Trust - Cyber Assurance</div>
#             <div class="subtitle">
#                 Enhancing trust in a digital world. Upload your audio files and let us take care of the rest!
#             </div>
#             <form action="/upload" method="post" enctype="multipart/form-data">
#                 <div class="upload-box">
#                     Drag and drop your MP3 or MP4 file here or click to select:
#                     <br><br>
#                     <input type="file" name="file" accept=".mp3,.mp4" required />
#                 </div>
#                 <br>
#                 <button type="submit" style="font-size: 1rem; padding: 10px 20px;">Upload File</button>
#             </form>
#             {download_button}
#             <div class="footer">© 2025 KPMG Digital Trust - Cyber Assurance Team</div>
#         </div>
#     </body>
#     </html>
#     """
#     return html_content

# # Route to handle file upload and processing
# @app.post("/upload")
# async def upload_file(file: UploadFile):
#     global is_file_ready
#     try:
#         # Save uploaded file
#         save_path = os.path.join(UPLOAD_DIR, file.filename)
#         with open(save_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         # Delete temporary files and process the uploaded file
#         delr()
#         main(save_path)
#         MOM("./transcription.txt")

#         # Ensure the processed files are created
#         if not os.path.exists("./transcription.txt") or not os.path.exists("./mom.txt"):
#             is_file_ready = False
#             return {"error": "File processing failed. Please try again."}

#         is_file_ready = True
#         return {"message": "File processed successfully. You can now download the files."}

#     except Exception as e:
#         is_file_ready = False
#         return {"error": f"An error occurred: {str(e)}"}

# # Route to handle downloading both files in a ZIP archive
# @app.get("/download-all")
# async def download_all_files():
#     try:
#         # Create a ZIP archive containing both files
#         zip_buffer = BytesIO()
#         with ZipFile(zip_buffer, "w") as zip_file:
#             zip_file.write("./transcription.txt", "transcription.txt")
#             zip_file.write("./mom.txt", "mom.txt")

#         zip_buffer.seek(0)

#         return StreamingResponse(
#             zip_buffer,
#             media_type="application/zip",
#             headers={"Content-Disposition": "attachment; filename=processed_files.zip"},
#         )

#     except Exception as e:
#         return {"error": f"An error occurred during file download: {str(e)}"}

# # Specify the port explicitly for Render deployment (use the environment variable `PORT` in Render)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))



