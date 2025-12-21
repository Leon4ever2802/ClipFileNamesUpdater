import re

CUTTED_MP4_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>[A-Za-z0-9 ]+?) (?P<date>\d{4}\.\d{2}\.\d{2})_?(?P<additional_info>[A-Za-z0-9_\-+]+)?'
               r'\.mp4$')

CUTTED_PNG_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>[A-Za-z0-9 ]+?) Screenshot (?P<date>\d{4}\.\d{2}\.\d{2})_?'
               r'(?P<additional_info>[A-Za-z0-9_\-+]+)?\.png$')

ADAPTED_MP4_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>[A-Za-z0-9_]+?)_(?P<date>\d{4}-\d{2}-\d{2})_?(?P<additional_info>[A-Za-z0-9_\-+]+)?'
               r'\.mp4$')

ADAPTED_PNG_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>[A-Za-z0-9_]+?)_Screenshot_(?P<date>\d{4}-\d{2}-\d{2})_?'
               r'(?P<additional_info>[A-Za-z0-9_\-+]+)?\.png$')
