# Tidier

Tidier is a simple command line tool that helps you make your files tidy up.
Examples will show you the power.

## Examples

After installing Tidier, using it is as easy as your moms cleans your room for you.

Copy all files inside `pictures` folder to `organized` folder organized by date:

```bash
$ tidier -i pictures -o organized
```

Move all files and organize by their year & type: (e.g. `/organized/2019/image/amir.png`)
```bash
$ tidier -i pictures -o organized --format "%Y/{type}" -m 
```

For all other options, see the output of `tidier --help`.


## Installing

To install the latest release from [PyPI](http://pypi.python.org/pypi/fabtools>)

``` bash
$ pip install tidier
```

To install the latest development version from [GitHub](https://github.com/itsamirhn/Tidier)

``` bash
$ pip install git+git://github.com/itsamirhn/tidier.git
```

## License

Tidier is MIT licensed.