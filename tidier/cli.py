"""The CLI commands"""
import locale
from typing import Tuple

import click

from .core import Path, find_sub_files


@click.command()
@click.argument(
    "input_path",
    type=click.Path(exists=True, path_type=Path, file_okay=False),
)
@click.option(
    "-o",
    "--output",
    "output_path",
    help="Output directory",
    default="./Tidier",
    type=click.Path(
        file_okay=False,
        writable=True,
        path_type=Path
    ))
@click.option(
    "-r",
    "--regex",
    "regex_replace",
    help="Regex match and replace",
    nargs=2,
    type=(str, str),
    default=(r"(.+)", r"%Y/%B/%d/\1"),
    show_default=True,
)
@click.option(
    "-e",
    "--exclude",
    "exclude_patterns",
    help="Excluding patterns",
    default=[],
    multiple=True,
)
@click.option(
    "-l",
    "--locale",
    "locale_code",
    help="Date and time locale",
    default="en_US",
    show_default=True,
)
@click.option(
    "-a",
    "--all",
    "all_files",
    help="Apply on all files including HIDDEN files",
    default=False,
    show_default=True,
    is_flag=True,
)
@click.option(
    "-j",
    "--jalali",
    "jalali_date",
    help="Use Jalali calendar",
    default=False,
    show_default=True,
    is_flag=True,
)
def main(
    input_path: Path,
    output_path: Path,
    regex_replace: str,
    exclude_patterns: Tuple[str],
    locale_code: str,
    all_files: bool,
    jalali_date: bool,
) -> None:
    """Tidy up the file & folder names"""
    locale.setlocale(locale.LC_ALL, locale_code)

    exclude_patterns = list(exclude_patterns)
    if not all_files:
        exclude_patterns.append("**/.*")

    regex, replacement = regex_replace[0], regex_replace[1]
    files = find_sub_files(input_path, regex, exclude_patterns)

    for file in files:
        old_path = file.path
        new_path = file.rename(regex, file.format(replacement, jalali_date), output_path)
        click.echo(f"[-] Moving {old_path} to {new_path}")


if __name__ == "__main__":
    main()
