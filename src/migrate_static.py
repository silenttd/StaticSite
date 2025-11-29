import os
import shutil

def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    os.mkdir(destination)
    
    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        
        if os.path.isfile(src_path):
  
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path}")
        else:
            copy_directory(src_path, dest_path)
