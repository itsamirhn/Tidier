from .utils import *


def organize(input_path: Path, output_path: Path, format_pattern: str, should_move: bool):
    files = []
    if input_path.is_file():
        files = [File(input_path)]
    if input_path.is_dir():
        files = find_sub_files(input_path)

    for file in files:
        path = file.organized_path(format_pattern, output_path)
        path.mkdir(parents=True, exist_ok=True)
        if should_move:
            file.move(path)
        else:
            file.copy(path)
