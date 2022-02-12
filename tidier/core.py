from pathlib import Path
import shutil
import datetime
import mimetypes


class File:

    ALLOWED_FORMATTERS = ['name', 'ext', 'type']

    def __init__(self, path: Path):
        if not path.is_file():
            raise ValueError
        self.path = path

    @property
    def name(self):
        return self.path.name

    @property
    def suffix(self):
        return self.path.suffix

    @property
    def ext(self):
        suffix = self.suffix
        if len(suffix) > 0:
            return suffix[1:]
        else:
            return 'unknown'

    @property
    def type(self):
        t = mimetypes.guess_type(self.name)[0]
        if t:
            t = t.split('/')[0]
            return t
        return 'unknown'

    @property
    def modified_date(self):
        mtime = datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        return mtime

    def copy(self, path: Path):
        shutil.copy2(self.path, path)

    def move(self, path: Path):
        shutil.move(self.path, path)

    @property
    def formatters_dict(self):
        dic = {}
        for formatter in self.ALLOWED_FORMATTERS:
            dic[formatter] = getattr(self, formatter)
        return dic

    def format(self, string: str):
        string = self.modified_date.strftime(string)
        return string.format(**self.formatters_dict)

    def __str__(self):
        return self.path.name
