# Tidier
[![PyPi version](https://badgen.net/pypi/v/tidier)](https://pypi.org/project/Tidier/)
[![PyPI license](https://img.shields.io/pypi/l/tidier.svg)](https://pypi.python.org/pypi/tidier/)
[![PyPI download month](https://img.shields.io/pypi/dm/tidier.svg)](https://pypi.python.org/pypi/tidier/)
[![GitHub stars](https://img.shields.io/github/stars/itsamirhn/tidier.svg?style=social&label=Star&maxAge=2592000)](https://github.com/itsamirhn/Tidier/stargazers/)


Tidier is a simple command line tool that helps you make your files tidy up.
Examples will show you the power.


## Examples

After installing Tidier, using it is as easy as your moms cleans your room for you.

**Move** all files inside `pictures` folder to `organized` folder organized by date:

```bash
$ tidier tidy "Pictures" -o "Organized"
```
Log output e.g. `[-] Moving Pictures/IMG_123.jpg to Organized/2018/April/01/IMG_123.jpg`

\
**Copy** all files and organize by their year & **type**:
```bash
$ tidier tidy "Pictures" -o "Organized" -r "%Y/{type}/{name}" --copy
```
Log e.g. `[-] Copying Pictures/IMG_123.jpg to Organized/2018/image/IMG_123.jpg`

\
**Move** all of your favorite show episodes to organized Season seperated folder:
```bash
$ tidier tvshow "Breaking Bad"
```
Log e.g. `[-] Moving Breaking Bad/breaking.bad.S04E03.x265.WEB-DL.mkv to Breaking Bad/Season 4 | x265 WEB-DL/Episode 3.mkv`


\
Also, you can use **Jalali** calendar date:

```bash
$ tidier tidy "Scripts" -r "%y/%B/{name}" --jalali
```
Log e.g. `[-] Moving Scripts/Crawler.py to Scripts/99/Ordibehesht/Crawler.py`

\
You can set **locale** or organize files by their **extension**:

```bash
$ tidier tidy "Valentine" -r "%Y %B/{ext}/{name}" --locale fr_FR
```
Log e.g. `[-] Moving Valentine/Paris.jpg to Valentine/2021 déc/Paris.jpg`

\
For all other options, see the output of `tidier --help`.


## Installing

To install the latest release from [PyPI](http://pypi.python.org/pypi/fabtools>):

``` bash
$ pip install tidier
```

To install the latest development version from [GitHub](https://github.com/itsamirhn/Tidier):

``` bash
$ pip install git+git://github.com/itsamirhn/tidier.git
```

## License

Tidier is MIT licensed.

---
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)