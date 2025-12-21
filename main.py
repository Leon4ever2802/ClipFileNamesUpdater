import os

from src.filename_adapters.mp4_adapter import adapt_mp4_filename
from src.filename_adapters.png_adapter import adapt_png_filename
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
}

for full_path, dirs, files in os.walk(GAME_CLIPS_PATH):
    if "Cutted" not in full_path or len(files) == 0:
        continue

    print(f"Checking game clips inside: {full_path}")

    files_adapted = 0

    for file_name in files:
        if file_name.lower().endswith(".mp4"):
            new_file_name = adapt_mp4_filename(file_name)
        if file_name.lower().endswith(".png"):
            new_file_name = adapt_png_filename(file_name)

        if new_file_name and file_name != new_file_name:
            file_path = os.path.join(full_path, file_name)
            new_file_path = os.path.join(full_path, new_file_name)

            os.rename(file_path, new_file_path)

            files_adapted = files_adapted + 1
            print(f"\tRenamed: {file_name} → {new_file_name}")

    if files_adapted == 0:
        print("\tNo adaptions made.")
