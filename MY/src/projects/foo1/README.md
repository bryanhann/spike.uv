# foo1

[![PyPI](https://img.shields.io/pypi/v/foo1.svg)](https://pypi.org/project/foo1/)
[![Changelog](https://img.shields.io/github/v/release/bryanhann/foo1?include_prereleases&label=changelog)](https://github.com/bryanhann/foo1/releases)
[![Tests](https://github.com/bryanhann/foo1/actions/workflows/test.yml/badge.svg)](https://github.com/bryanhann/foo1/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/bryanhann/foo1/blob/master/LICENSE)



## Installation

Install this tool using `pip`:
```bash
pip install foo1
```
## Usage

For help, run:
```bash
foo1 --help
```
You can also use:
```bash
python -m foo1 --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd foo1
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
