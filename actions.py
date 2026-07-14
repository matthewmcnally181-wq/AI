import os
import shutil

def organize_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for file in os.listdir(source):
        file_path = os.path.join(source, file)

        if os.path.isfile(file_path):
            ext = file.split('.')[-1]
            ext_folder = os.path.join(destination, ext)

            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            shutil.move(file_path, os.path.join(ext_folder, file))

    return f"Files organized from {source} → {destination}"


def create_folder(destination):
    os.makedirs(destination, exist_ok=True)
    return f"Folder created: {destination}"


def move_file(source, destination):
    shutil.move(source, destination)
    return f"Moved {source} → {destination}"