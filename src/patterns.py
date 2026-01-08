import re

CUTTED_MP4_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>[\w\- ]+?) (?P<date>\d{4}\.\d{2}\.\d{2})(?:_(?P<additional_info>[\w\-+]+))?.*'
               r'\.mp4$', re.MULTILINE)

CUTTED_PNG_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>[\w\- ]+?) Screenshot (?P<date>\d{4}\.\d{2}\.\d{2})(?:_(?P<additional_info>[\w\-+]+))?.*'
               r'\.png$', re.MULTILINE)

ADAPTED_MP4_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>\w+?)_(?P<date>\d{4}-\d{2}-\d{2})(?:_(?P<additional_info>[\w\-+]+))?\.mp4$', re.MULTILINE)

ADAPTED_PNG_FILE_PATTERN = \
    re.compile(r'^(?P<game_name>\w+?)_Screenshot_(?P<date>\d{4}-\d{2}-\d{2})(?:_(?P<additional_info>[\w\-+]+))?\.png$', re.MULTILINE)
