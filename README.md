# Tidier

Tidier is a simple command line tool that helps you make your files tidy up.
Examples will show you the power.

## Examples

After installing Tidier, using it is as easy as your moms cleans your room for you.

**Copy** all files inside `pictures` folder to `organized` folder organized by date:

```bash
$ tidier -i pictures -o organized
```
\
**Move** all files and organize by their year & **type**:
```bash
$ tidier -i pictures -o organized --format "%Y/{type}" -m 
```
output e.g. `/organized/2019/image/Amir.jpeg`

\
Also, you can use **Jalali** calendar date:

```bash
$ tidier -i codes -o organized --format "%y/%B" --jalali
```
output e.g. `/organized/99/Bahman/main.cpp`

\
You can set **locale** or organize files by their **extension**:

```bash
$ tidier -i valentine -o organized --format "%Y %B/{ext}" --locale fr_FR
```
output e.g. `/organized/2021 déc/png/paris.png`

\
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