from setuptools import setup, find_packages

setup(
    name="Tidier",
    version="0.5.3",
    packages=find_packages(),
    url="https://github.com/itsamirhn/Tidier",
    download_url="https://github.com/itsamirhn/Tidier/archive/refs/tags/v0.5.3.tar.gz",
    license="MIT",
    author="AmirMohammad Hosseini Nasab",
    author_email="awmirhn@gmail.com",
    description="A tool for organizing files",
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
)
