import tidier
import click


@click.command()
@click.option("-i", "--input", "input_path",
              help="Input directory or file.",
              required=True,
              type=click.Path(
                  exists=True,
                  path_type=tidier.Path
              ))
@click.option("-o", "--output", "output_path",
              help="Output directory.",
              default="",
              type=click.Path(
                  file_okay=False,
                  writable=True,
                  path_type=tidier.Path
              ))
@click.option("-f", "--format", "format_pattern",
              help="Folders format.",
              default="%Y/%B/%d",
              show_default=True)
@click.option("-m", "--move", "should_move",
              help="Move input instead of copy.",
              default=False,
              is_flag=True)
def organize(input_path: tidier.Path, output_path: tidier.Path, format_pattern: str, should_move: bool):
    tidier.organize(input_path, output_path, format_pattern, should_move)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    organize()


