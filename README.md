# Poetry Plugin Import

[![License: LGPL v3](https://img.shields.io/badge/License-MIT-blue.svg)](https://mit-license.org)
![PyPI](https://img.shields.io/pypi/pyversions/poetry-plugin-import)
![PyPI](https://img.shields.io/pypi/v/poetry-plugin-import?color=gree&label=pypi%20package)
[![Python application](https://github.com/neriberto/poetry-plugin-import/actions/workflows/python-app.yml/badge.svg)](https://github.com/neriberto/poetry-plugin-import/actions/workflows/python-app.yml)

A [Poetry](https://python-poetry.org) plugin that import dependencies from requirements.txt.

## Installation

In order to install the plugin you need to have installed a poetry version `>1.2.2` and type:

```bash
poetry self add poetry-plugin-import
```

## Usage

Imagine the following requirements.txt that you want to import into you pyproject.html

```toml
asyncio==3.4.3
git+https://github.com/neriberto/malwarefeeds.git@0.1.0#egg=malwarefeeds
requests==2.22.0
click==7.0
```

then, to import just run the command below:

```bash
poetry import
```

## License

This project is licensed under the terms of the MIT license.