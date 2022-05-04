from setuptools import setup, find_packages

setup(
    name="Tidier",
    version="0.4.4",
    packages=find_packages(),
    url="https://github.com/itsamirhn/Tidier",
    download_url="https://github.com/itsamirhn/Tidier/archive/refs/tags/v0.4.4.tar.gz",
    license="MIT",
    author="AmirMohammad Hosseini Nasab",
    author_email="awmirhn@gmail.com",
    description="A tool for organizing files",
    install_requires=[
        "Click",
        "jdatetime",
    ],
    entry_points={
        "console_scripts": [
            "tidier=tidier.cli:main",
        ],
    },
)
