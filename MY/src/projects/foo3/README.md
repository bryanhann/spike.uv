# foo3

[![PyPI](https://img.shields.io/pypi/v/foo3.svg)](https://pypi.org/project/foo3/)
[![Changelog](https://img.shields.io/github/v/release/bryanhann/foo3?include_prereleases&label=changelog)](https://github.com/bryanhann/foo3/releases)
[![Tests](https://github.com/bryanhann/foo3/actions/workflows/test.yml/badge.svg)](https://github.com/bryanhann/foo3/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/bryanhann/foo3/blob/master/LICENSE)



## Installation

Install this tool using `pip`:
```bash
pip install foo3
```
## Usage

For help, run:
```bash
foo3 --help
```
You can also use:
```bash
python -m foo3 --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd foo3
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
