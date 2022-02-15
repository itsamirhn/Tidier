"""The Classes and Logic of the Tidier"""
import datetime
import mimetypes
import shutil
from pathlib import Path

import jdatetime


class File:
    """File object with given path"""

    ALLOWED_FORMATTERS = ["name", "ext", "type"]

    def __init__(self, path: Path) -> None:
        """Description

        Args:
            path (Path) : Desired file's path.

        Returns:
            None

        Raises:
            ValueError : Given path is not a file.
        """
        if not path.is_file():
            raise ValueError
        self.path = path

    @property
    def name(self) -> str:
        """Finding name of the file using `path`.

        Returns:
            File's name
        """
        return self.path.name

    @property
    def suffix(self) -> str:
        """Finding suffix of the file using `path`.

        Returns:
            File's suffix
        """
        return self.path.suffix

    @property
    def ext(self) -> str:
        """Finding extension of the file using file's suffix.

        Returns:
            File's Extension
        """
        suffix = self.suffix
        if len(suffix) > 0:
            output = suffix[1:]
        else:
            output = "unknown"
        return output

    @property
    def type(self) -> str:
        """Guess the type of the file using `mimetypes`.

        Returns:
            File's type
        """
        guess_type = mimetypes.guess_type(self.name)[0]
        if guess_type:
            guess_type = guess_type.split("/")[0]
            return guess_type
        return "unknown"

    @property
    def modified_date(self) -> datetime.datetime:
        """Finding modified date & time.

        Returns:
            File's Modified DateTime
        """
        mtime = datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        return mtime

    def copy(self, path: Path) -> None:
        """Copy the file to given path.

        Args:
            path (Path) : the path that file should be copied to.

        Returns:
            None
        """
        shutil.copy2(self.path, path)

    def move(self, path: Path) -> None:
        """Move the file to given path.

        Args:
            path (Path) : the path that file should be moved to.

        Returns:
            None
        """
        shutil.move(self.path, path)

    @property
    def formatters_dict(self) -> dict:
        """Getting dictionary of file's attributes than can be use in formatting

        Returns:
            Dictionary of file's attributes
        """
        dic = {}
        for formatter in self.ALLOWED_FORMATTERS:
            dic[formatter] = getattr(self, formatter)
        return dic

    def format(self, string: str, jalali_date: bool) -> str:
        """Getting dictionary of file's attributes than can be use in formatting

        Args:
            string (str) : String to be formatted
            jalali_date (bool) : Flag to use `Jalali Calendar` or not

        Returns:
            Formatted string
        """
        if jalali_date:
            date = jdatetime.datetime.fromgregorian(datetime=self.modified_date)
        else:
            date = self.modified_date
        string = date.strftime(string)
        return string.format(**self.formatters_dict)

    def __str__(self) -> str:
        """"""
        return self.name
