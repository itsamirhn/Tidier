"""Helper utilities"""
from typing import List, Iterable

from .classes import Path, File


def find_sub_files(dir_path: Path, match_regex: str = None, exclude_patterns: Iterable[str] = None) -> List[File]:
    """Find all files in given path matching with regex and exclude some

    Args:
        dir_path (Path) : Directory path to search files in
        exclude_patterns (Iterable[str]) : Patterns to exclude in finding files
        match_regex (str, optional): Search regex to filter files. Defaults to None.

    Return:
        List of founded Files object
    """

    all_sub_paths = dir_path.glob("**/*")
    excluded_paths: List[str] = []
    for pattern in exclude_patterns:
        excluded_paths += dir_path.glob(pattern)
    paths = [
        path
        for path in all_sub_paths
        if path not in excluded_paths
    ]
    files = [
        File(path)
        for path in paths
        if path.is_file()
    ]
    return list(filter(lambda file: file.match(match_regex), files))
