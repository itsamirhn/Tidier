"""Helper utilities"""
from typing import List, Iterable

from tidier.core import Path, File


def find_sub_files(path: Path, exclude_patterns: Iterable[str]) -> List[File]:
    """Find all files in given path and exclude some

    Args:
        path (Path) : Path to search files in
        exclude_patterns (Iterable[str]) : Patterns to exclude in finding files

    Return:
        List of founded Files object
    """
    all_sub_paths = path.glob("**/*")
    excluded_paths: List[str] = []
    for pattern in exclude_patterns:
        excluded_paths += path.glob(pattern)
    files = [
        File(path)
        for path in all_sub_paths
        if path.is_file() and path not in excluded_paths
    ]
    return files
