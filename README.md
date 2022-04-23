# Tidier

Tidier is a simple command line tool that helps you make your files tidy up.
Examples will show you the power.

## Examples

After installing Tidier, using it is as easy as your moms cleans your room for you.

**Move** all files inside `pictures` folder to `organized` folder organized by date:

```bash
$ tidier pictures -o organized
```
Output e.g. `[-] Moving pictures/IMG_123.jpg to organized/2018/April/01/IMG_123.jpg`

\
**Copy** all files and organize by their year & **type**:
```bash
$ tidier pictures -o organized -r "%Y/{type}/{name}" --copy
```
Output e.g. `[-] Copying pictures/IMG_123.jpg to organized/2018/image/IMG_123.jpg`

\
**Move** all of your favorite show episodes to organized Season seperated folder:
```bash
$ tidier 'Breaking Bad' -m '.*S0*(\d)E0*(\d).*' -r "Season \1/Episode \2.{ext}"
```
Output e.g. `[-] Moving Breaking Bad/breaking.bad.S04E03 to Breaking Bad/Season 4/Episode 3.mkv`


\
Also, you can use **Jalali** calendar date:

```bash
$ tidier codes -o organized -r "%y/%B/{name}" --jalali
```
Output e.g. `[-] Moving pictures/IMG_123.jpg to organized/99/Ordibehesht/IMG_123.jpg`

\
You can set **locale** or organize files by their **extension**:

```bash
$ tidier valentine -o organized -r "%Y %B/{ext}/{name}" --locale fr_FR
```
Output e.g. `[-] Moving pictures/Paris.jpg to organized/2021 déc/Paris.jpg`

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