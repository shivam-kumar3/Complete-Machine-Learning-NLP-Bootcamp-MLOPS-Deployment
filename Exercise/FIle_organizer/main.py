import os
import shutil

path = input('Enter the Path')
files = os.listdir(path)

for file in files:
    filenames, extension = os.path.splitext(file)
    print(filenames , extension)

    full_file_path = os.path.join(path, file)

    # Handle files with no extension
    if extension == '':
        extension = 'no_extension'
        
    # Create a directory for the extension if it doesn't exist
    destination_dir = os.path.join(path, extension)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        
        # Move the file to the respective extension folder
        shutil.move(full_file_path, os.path.join(destination_dir, file))
