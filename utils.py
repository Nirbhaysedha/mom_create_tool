import os
import shutil

def delr():
    folder_path = '/Users/nirbhaysedha/Desktop/S2T/temp'  # Replace with the actual path to the folder
    file_path1 = '/Users/nirbhaysedha/Desktop/S2T/transcription.txt'  # Replace with the actual path to the file
    file_path2= '/Users/nirbhaysedha/Desktop/S2T/MoM.txt' 

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    if os.path.exists(file_path1):
        os.remove(file_path1)
    if os.path.exists(file_path2):
        os.remove(file_path2)
