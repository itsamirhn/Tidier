from typing import List, Iterable

from core import *


def find_sub_files(path: Path, exclude_patterns: Iterable[str]) -> List[File]:
    all_sub_paths = path.glob('**/*')
    excluded_paths = []
    for pattern in exclude_patterns:
        excluded_paths += path.glob(pattern)
    files = [File(path) for path in all_sub_paths if path.is_file() and path not in excluded_paths]
    return files
