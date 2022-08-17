from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

def license():
    with open('LICENSE.txt') as f:
        return f.read()


setup(
    name="Tidier",
    version="0.5.4",
    packages=find_packages(),
    url="https://github.com/itsamirhn/Tidier",
    download_url="https://github.com/itsamirhn/Tidier/archive/refs/tags/v0.5.4.tar.gz",
    license=license(),
    author="AmirMohammad Hosseini Nasab",
    author_email="awmirhn@gmail.com",
    description="A tool for organizing files",
    long_description=readme(),
    install_requires=[
        "Click",
        "jdatetime",
        "pathlib",
    ],
    entry_points={
        "console_scripts": [
            "tidier=tidier.cli:cli",
        ],
    },
    python_requires='>=3',
)
