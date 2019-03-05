from setuptools import setup
import os.path

# Get the version:
version = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'version.py')) as f: exec(f.read(), version)

setup(
    name = 'ctupdate',
    version = version['__version__'],
    description = 'A simple script to bulk update file ctime attributes',
    author = 'Alastair Droop',
    author_email = 'alastair.droop@gmail.com',
    url = 'https://github.com/alastair.droop/ctupdate',
    classifiers = [
        'Programming Language :: Python'
    ],
    py_modules = ['ctupdate', 'version'],
    install_requires = [
        'argparse'
    ],
    python_requires = '>=2.7',
    entry_points = {
        'console_scripts': [
            'ctupdate=ctupdate:main'
        ]
    }
)
