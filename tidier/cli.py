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
    "-m",
    "--match",
    "regex_match",
    help="Regex match",
    type=str,
    default="^(.+)$",
    show_default=True,
)
@click.option(
    "-r",
    "--replace",
    "regex_replace",
    help="Regex replace",
    type=str,
    default=r"%Y/%B/%d/{name}",
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
    "-c",
    "--copy",
    "should_copy",
    help="Copy files instead of Move",
    default=False,
    show_default=True,
    is_flag=True,
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
    regex_match: str,
    regex_replace: str,
    exclude_patterns: Tuple[str],
    should_copy: bool,
    locale_code: str,
    all_files: bool,
    jalali_date: bool,
) -> None:
    """Tidy up the file & folder names"""
    locale.setlocale(locale.LC_ALL, locale_code)

    exclude_patterns = list(exclude_patterns)
    if not all_files:
        exclude_patterns.append("**/.*")

    files = find_sub_files(input_path, regex_match, exclude_patterns)

    for file in files:
        old_path = file.path
        new_path = file.rename(regex_match, file.format(regex_replace, jalali_date), output_path, should_copy)
        click.echo(f"[-] {'Copying' if should_copy else 'Moving'} {old_path} to {new_path}")


if __name__ == "__main__":
    main()
