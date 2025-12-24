from config import config
from update_file_names import update_file_names

def main():
    update_file_names(config.get("GAME_CLIPS_PATH"))

if __name__ == "__main__":
    main()