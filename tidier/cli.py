from typing import Tuple
import locale
from utils import *
import click


@click.command()
@click.option("-i", "--input", "input_path",
              help="Input directory or file",
              required=True,
              type=click.Path(
                  exists=True,
                  path_type=Path
              ))
@click.option("-o", "--output", "output_path",
              help="Output directory",
              default="",
              type=click.Path(
                  file_okay=False,
                  writable=True,
                  path_type=Path
              ))
@click.option("-f", "--format", "format_pattern",
              help="Folders format",
              default="%Y/%B/%d/{type}",
              show_default=True)
@click.option("-e", "--exclude", "exclude_patterns",
              help="Excluding patterns",
              default=[],
              multiple=True)
@click.option("-l", "--locale", "locale_code",
              help="Date and time locale",
              default="en_US",
              show_default=True)
@click.option("-m", "--move", "should_move",
              help="Move input file(s) instead of copy",
              default=False,
              show_default=True,
              is_flag=True)
@click.option("-a", "--all", "all_files",
              help="Apply on all files including HIDDEN files",
              default=False,
              show_default=True,
              is_flag=True)
@click.option("-j", "--jalali", "jalali_date",
              help="Use Jalali calendar",
              default=False,
              show_default=True,
              is_flag=True)
def main(input_path: Path,
         output_path: Path,
         format_pattern: str,
         exclude_patterns: Tuple[str],
         locale_code: str,
         should_move: bool,
         all_files: bool,
         jalali_date: bool):

    exclude_patterns = list(exclude_patterns)
    if not all_files:
        exclude_patterns.append('**/.*')

    files = []
    if input_path.is_file():
        files = [File(input_path)]
    if input_path.is_dir():
        files = find_sub_files(input_path, exclude_patterns)

    locale.setlocale(locale.LC_ALL, locale_code)
    for file in files:
        path = output_path / file.format(format_pattern, jalali_date)
        path.mkdir(parents=True, exist_ok=True)
        if should_move:
            click.echo(f"[-] Moving {file.path} to {path}")
            file.move(path)
        else:
            click.echo(f"[-] Copying {file.path} to {path}")
            file.copy(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


