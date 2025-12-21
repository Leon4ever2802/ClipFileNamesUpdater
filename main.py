from update_file_names import update_file_names
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
}

update_file_names(config.get("GAME_CLIPS_PATH"))
