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
        ctime = datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        return ctime

    def copy(self, path):
        shutil.copy2(self.path, path)

    def __str__(self):
        return self.path.name


class Folder:

    def __init__(self, path: Path, make=True):
        if make:
            path.mkdir(parents=True, exist_ok=True)
        if not path.is_dir():
            raise ValueError
        self.path = path

    def sub_files(self):
        all_sub_paths = self.path.glob('**/*')
        files = [File(path) for path in all_sub_paths if path.is_file()]
        return files
