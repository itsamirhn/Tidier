"""Description about file."""
import datetime
import mimetypes
import shutil
from pathlib import Path
import jdatetime


class File:
    """Description about class"""
    ALLOWED_FORMATTERS = ["name", "ext", "type"]

    def __init__(self, path: Path) -> None:
        """Description

        Args:
            path (Path) : description about path.

        Returns:
            None

        Raises:
            ValueError : ValueError detail.
        """
        if not path.is_file():
            raise ValueError
        self.path = path

    @property
    def name(self) -> str:
        """
        """
        return self.path.name

    @property
    def suffix(self) -> str:
        """
        """
        return self.path.suffix

    @property
    def ext(self) -> str:
        """"""
        suffix = self.suffix
        if len(suffix) > 0:
            output = suffix[1:]
        else:
            output =  "unknown"
        return output

    @property
    def type(self) -> str:
        """"""
        t = mimetypes.guess_type(self.name)[0]
        if t:
            t = t.split("/")[0]
            return t
        return "unknown"

    @property
    def modified_date(self) -> datetime.datetime:
        """"""
        mtime = datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        return mtime

    def copy(self, path: Path) -> None:
        """"""
        shutil.copy2(self.path, path)

    def move(self, path: Path) -> None:
        """"""
        shutil.move(self.path, path)

    @property
    def formatters_dict(self) -> dict:
        """"""
        dic = {}
        for formatter in self.ALLOWED_FORMATTERS:
            dic[formatter] = getattr(self, formatter)
        return dic

    def format(self, string: str, jalali_date: bool) -> str:
        """"""
        if jalali_date:
            date = jdatetime.datetime.fromgregorian(datetime=self.modified_date)
        else:
            date = self.modified_date
        string = date.strftime(string)
        return string.format(**self.formatters_dict)

    def __str__(self) -> str:
        """"""
        return self.path.name
