import click
from pathlib import Path
from tidy import File, Folder


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
              default="output",
              type=click.Path(
                  file_okay=False,
                  writable=True,
                  path_type=Path
              ))
@click.option("-f", "--format", "format_pattern",
              help="Folders format.",
              default="%Y/%B/%d",
              show_default=True,
              type=click.STRING)
def main(input_path: Path, output_path: Path, format_pattern: str):
    files = []
    if input_path.is_file():
        files = [File(input_path)]
    if input_path.is_dir():
        files = Folder(input_path).sub_files()

    for file in files:
        path = output_path / file.modified_date.strftime(format_pattern)
        path.mkdir(parents=True, exist_ok=True)
        file.copy(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


