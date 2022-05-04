"""The CLI commands"""
import locale
import random
from typing import Tuple

import click

from tidier.core import Path, find_sub_files


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
    default=None,
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
@click.option(
    "--log",
    help="Full log for changed paths",
    default=False,
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
        log: bool,
) -> None:
    """Tidy up the file & folder names"""
    locale.setlocale(locale.LC_ALL, locale_code)

    exclude_patterns = list(exclude_patterns)
    if not all_files:
        exclude_patterns.append("**/.*")

    files = find_sub_files(input_path, regex_match, exclude_patterns)

    failed_files = []
    changed_paths = []
    with click.progressbar(files, item_show_func=lambda x: x.path.__str__() if x else "Done!") as files_bar:
        for file in files_bar:
            try:
                old_path = file.path
                new_path = file.rename(regex_match, file.format(regex_replace, jalali_date), output_path, should_copy)
                changed_paths.append((old_path, new_path))
            except Exception as e:
                failed_files.append((file, e))

    if failed_files:
        with open(Path.cwd() / "tidier_fails.txt", "w") as f:
            for file, error in failed_files:
                f.write(f"{file.path}\n")
        click.secho(f"[!] Failed files are saved to {Path.cwd() / 'tidier_fails.txt'}", err=True, fg="yellow")

    if log:
        for old_path, new_path in changed_paths:
            click.secho(f"{'Copied' if should_copy else 'Moved'} {old_path} to {new_path}", fg="green")
        for file, error in failed_files:
            click.secho(f"[!] Failed {'copying' if should_copy else 'moving'} {file.path} due: {error}", err=True, fg="red")


if __name__ == "__main__":
    main()
