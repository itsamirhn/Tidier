from typing import List

from .core import *


def find_sub_files(path: Path) -> List[File]:
    all_sub_paths = path.glob('**/*')
    files = [File(path) for path in all_sub_paths if path.is_file()]
    return files
