from setuptools import setup

setup(
    name='Tidier',
    version='0.1',
    packages=['tidier'],
    url='https://github.com/itsamirhn/Tidier',
    download_url='https://github.com/itsamirhn/Tidier/archive/refs/tags/v0.1.tar.gz',
    license='MIT',
    author='AmirMohammad Hosseini Nasab',
    author_email='awmirhn@gmail.com',
    description='A tool for organizing files',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'tidier=tidier.cli:main',
        ],
    },
)
