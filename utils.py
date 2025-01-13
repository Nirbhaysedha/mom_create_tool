import os
import shutil

def delr():
    folder_path = './temp'  # Replace with the actual path to the folder
    file_path1 = './transcription.txt'  # Replace with the actual path to the file
    file_path2= './MoM.txt' 

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    if os.path.exists(file_path1):
        os.remove(file_path1)
    if os.path.exists(file_path2):
        os.remove(file_path2)
