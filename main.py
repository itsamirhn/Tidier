from typing import Tuple

import click
from tidy import *


@click.command()
@click.option("-i", "--input", "input_path",
              help="Input directory or file.",
              required=True,
              type=click.Path(
                  exists=True,
                  path_type=Path
              ))
@click.option("-o", "--output", "output_path",
              help="Output directory.",
              default="",
              type=click.Path(
                  file_okay=False,
                  writable=True,
                  path_type=Path
              ))
@click.option("-f", "--format", "format_pattern",
              help="Folders format.",
              default="%Y/%B/%d",
              show_default=True)
def organize(input_path: Path, output_path: Path, format_pattern: str):
    files = []
    if input_path.is_file():
        files = [File(input_path)]
    if input_path.is_dir():
        files = find_sub_files(input_path)

    for file in files:
        path = file.organized_path(format_pattern, output_path)
        path.mkdir(parents=True, exist_ok=True)
        file.copy(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    organize()


