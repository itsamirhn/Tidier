"""The CLI commands"""
import locale
from typing import Tuple

import click

from tidier.core import Path, find_sub_files


def main(
        input_path: str,
        output_path: str,
        regex_match: str,
        regex_replace: str,
        exclude_patterns: Tuple,
        should_copy: bool,
        locale_code: str,
        all_files: bool,
        jalali_date: bool,
        log: bool,
        silent: bool = False,
) -> None:
    """Custom full option command for organizing files"""
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path
    output_path = Path(output_path)

    locale.setlocale(locale.LC_ALL, locale_code)

    exclude_patterns = list(exclude_patterns)
    if not all_files:
        exclude_patterns.append("**/.*")

    files = find_sub_files(input_path, regex_match, exclude_patterns)

    if silent:
        for file in files:
            try:
                formatted_path = file.formatter(regex_replace, jalali_date)
                file.rename(regex_match, formatted_path, output_path, should_copy)
            except Exception as e:
                pass
        return

    failed_files = []
    changed_paths = []
    with click.progressbar(files, item_show_func=lambda x: x.path.__str__() if x else "Done!") as files_bar:
        for file in files_bar:
            try:
                old_path = file.path
                formatted_path = file.formatter(regex_replace, jalali_date)
                new_path = file.rename(regex_match, formatted_path, output_path, should_copy)
                changed_paths.append((old_path, new_path))
            except Exception as e:
                failed_files.append((file, e))
    if failed_files:
        with open(Path.cwd() / "tidier_fails.txt", "a") as f:
            for file, error in failed_files:
                f.write(f"{file.path}\n")
        click.secho(f"[!] Failed files are saved to {Path.cwd() / 'tidier_fails.txt'}", err=True, fg="yellow")

    if log:
        for old_path, new_path in changed_paths:
            click.secho(f"{'Copied' if should_copy else 'Moved'} {old_path} to {new_path}", fg="green")
        for file, error in failed_files:
            click.secho(f"[!] Failed {'copying' if should_copy else 'moving'} {file.path} due: {error}", err=True,
                        fg="red")


@click.group()
def cli():
    """Tidier CLI"""
    pass


@cli.command()
@click.argument(
    "input_path",
    type=click.Path(exists=True, file_okay=False),
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
def tidy(
        input_path: str,
        output_path: str,
        regex_match: str,
        regex_replace: str,
        exclude_patterns: Tuple[str],
        should_copy: bool,
        locale_code: str,
        all_files: bool,
        jalali_date: bool,
        log: bool,
) -> None:
    """Custom full option command for organizing files"""
    main(input_path, output_path, regex_match, regex_replace, exclude_patterns, should_copy, locale_code, all_files, jalali_date, log)


@cli.command("tvshow")
@click.argument(
    "input_path",
    type=click.Path(exists=True, file_okay=False),
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
    ))
@click.option(
    "--ignore-subtitles",
    help="Ignore subtitles",
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
def tv_show(
        input_path: str,
        output_path: str,
        ignore_subtitles: bool,
        log: bool
) -> None:
    """Auto Tidy TV Shows Episodes"""
    click.secho("[+] Cleaning Episodes name...", fg="green")
    main(
        input_path,
        output_path,
        r"_",
        r" ",
        (),
        False,
        "en_US",
        False,
        False,
        log,
    )
    click.secho("[+] Adding Episodes to Folders...", fg="green")
    main(
        input_path,
        output_path,
        r"^.*(S|s)0*(?P<season>\d{1,2})(E|e)0*(?P<episode>\d{1,2})(?P<extra>.*)\.(?P<ext>mkv|mp4)$",
        r"Season \g<season> | \g<extra>/Episode \g<episode>.\g<ext>",
        (),
        False,
        "en_US",
        False,
        False,
        log
    )
    if not ignore_subtitles:
        click.secho("[+] Searching subtitles...", fg="green")
        main(
            input_path,
            output_path,
            r"^.*(S|s)0*(?P<season>\d{1,2})(E|e)0*(?P<episode>\d{1,2}).*\.(?P<ext>srt|ssa)$",
            r"Season \g<season> | Subtitles/Episode \g<episode>.\g<ext>",
            (),
            False,
            "en_US",
            False,
            False,
            log
        )


if __name__ == "__main__":
    cli()
