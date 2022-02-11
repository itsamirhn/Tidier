from pathlib import Path
import shutil
import datetime


class File:

    def __init__(self, path: Path):
        if not path.is_file():
            raise ValueError
        self.path = path

    @property
    def modified_date(self):
        mtime = datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        return mtime

    def organized_path(self, format_pattern: str, root_path=Path('')):
        mtime = self.modified_date
        path = root_path / mtime.strftime(format_pattern)
        return path

    def copy(self, path: Path):
        shutil.copy2(self.path, path)

    def move(self, path: Path):
        shutil.move(self.path, path)

    def __str__(self):
        return self.path.name
