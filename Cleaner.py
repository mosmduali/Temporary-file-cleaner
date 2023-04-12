# Github: https://github.com/muhammedosmanduali
# Linkedin: https://www.linkedin.com/in/muhammedosmanduali/

import os, shutil
import datetime

date = datetime.datetime.now()
# Get username
username = os.getlogin()
# Folder paths
paths = ["C:/Windows/Temp/",f"C:/Users/{username}/AppData/Local/Temp/","C:/Windows/Prefetch/"]
# Counters
others = 0
folders = 0
notDeleteds = 0

# A for loop that loops through paths one by one
for i in range(3):
     # Returns a list containing the names of files and folders in the specified directory
     for path in os.listdir(paths[i]):
          # Concatenates the specified directory paths to create a path string containing one or more subdirectory paths and filenames
          folderPath = os.path.join(paths[i], path) 
          try:
               # Checks if the specified path points to a file
               if os.path.isfile(folderPath):
                    # Deletes the specified file
                    os.remove(folderPath)
                    others +=1
               # Checks if the specified path points to a directory
               elif os.path.isdir(folderPath):
                    # Permanently deletes the specified directory and its subdirectories
                    shutil.rmtree(folderPath)
                    folders +=1
          # This error block works when the file or directory cannot be deleted
          except Exception as Error:
               notDeleteds +=1;
# Outputs a .txt extension to the downloads folder
with open(f"C:/Users/{username}/Downloads/Output.txt", "a") as f:
     f.write(f"Date: {date.day}")
     f.write(f".{date.month}")
     f.write(f".{date.year}\thour: {date.hour}:{date.minute}")
     f.write("\n")
     f.write(f"Paths: {paths[0]}, {paths[1]}, {paths[2]}")
     f.write("\n")
     f.write(f"Folders: {folders}, Others: {others}, Indelible: {notDeleteds}")
     f.write("\n\n")
     
