import os

from src.filename_adapters.mp4_file_name_adapter import adapt_mp4_file_name
from src.filename_adapters.png_file_name_adapter import adapt_png_file_name

def update_file_names(game_clips_path :str):
    files_adapted: int = 0

    for path, _dirs, files in os.walk(game_clips_path):
        if "Cutted" not in path or len(files) == 0:
            continue

        file_name_update_made_in_path: bool = False

        print(f"Checking game clips inside: {path}")

        for file_name in files:
            if file_name.lower().endswith(".mp4"):
                new_file_name = adapt_mp4_file_name(file_name)
            if file_name.lower().endswith(".png"):
                new_file_name = adapt_png_file_name(file_name)
            else:
                print(f"\t{file_name} is not a mp4/png file.")
                continue

            if new_file_name and file_name != new_file_name:
                file_path = os.path.join(path, file_name)
                new_file_path = os.path.join(path, new_file_name)

                os.rename(file_path, new_file_path)

                file_name_update_made_in_path = True
                files_adapted += 1
                print(f"\tRenamed: {file_name} → {new_file_name}")

        if not file_name_update_made_in_path:
            print("\tNo filename updates made.")

    print(f"{files_adapted} files were updated.")