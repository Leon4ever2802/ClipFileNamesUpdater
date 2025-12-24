from re import Pattern

from config import config
from replacement_dict import known_games
from src.patterns import ADAPTED_PNG_FILE_PATTERN, CUTTED_PNG_FILE_PATTERN, CUTTED_MP4_FILE_PATTERN, \
    ADAPTED_MP4_FILE_PATTERN

def __adapt_file_name(file_name: str, adapted_pattern: Pattern[str], cutted_pattern: Pattern[str], after_game_name_text: str, file_type: str) -> str | None:
    if adapted_pattern.match(file_name):
        return None

    try:
        cutted_match_dict = cutted_pattern.match(file_name).groupdict()

        cutted_game_name = cutted_match_dict.get("game_name").strip()

        if known_games.get(cutted_game_name) and config.get("ENABLE_REPLACEMENT_NAMES"):
            cutted_game_name = known_games.get(cutted_game_name)

        new_file_name = f"{cutted_game_name.replace(' ', '_')}{after_game_name_text}{cutted_match_dict.get('date').replace('.', '-')}.{file_type}"

        if cutted_match_dict.get('additional_info'):
            # [:-4] because we don't want the file type
            new_file_name = f"{new_file_name[:-4]}_{cutted_match_dict.get('additional_info')}.{file_type}"

        return new_file_name

    except AttributeError:
        print(f"\t{file_name} has an invalid filename structure!")
        return None

def adapt_mp4_file_name(file_name: str) -> str | None:
    return __adapt_file_name(file_name, ADAPTED_MP4_FILE_PATTERN, CUTTED_MP4_FILE_PATTERN, "_", "mp4")


def adapt_png_file_name(file_name: str) -> str | None:
    return __adapt_file_name(file_name, ADAPTED_PNG_FILE_PATTERN, CUTTED_PNG_FILE_PATTERN, "_Screenshot_", "png")
