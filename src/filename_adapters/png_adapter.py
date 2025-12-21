from game_dicts import known_games
from src.patterns import ADAPTED_PNG_FILE_PATTERN, CUTTED_PNG_FILE_PATTERN


def adapt_png_filename(file_name: str) -> str | None:
    if ADAPTED_PNG_FILE_PATTERN.match(file_name):
        return None

    try:
        cutted_match_dict = CUTTED_PNG_FILE_PATTERN.match(file_name).groupdict()

        cutted_game_name = cutted_match_dict.get("game_name").strip()

        if known_games.get(cutted_game_name):
            cutted_game_name = known_games.get(cutted_game_name)

        new_file_name = f"{cutted_game_name.replace(' ', '_')}_Screenshot_{cutted_match_dict.get('date').replace('.', '-')}.png"

        if cutted_match_dict.get('additional_info'):
            # [:-4] because we don't want the file type
            new_file_name = f"{new_file_name[:-4]}_{cutted_match_dict.get('additional_info')}.png"

        return new_file_name

    except AttributeError:
        print(f"\t{file_name} has an invalid filename structure!")
        return None
