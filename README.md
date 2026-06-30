# aznum2words - Azerbaijani Number to Words Converter for Python

`aznum2words` is a lightweight Python library for converting numbers to
Azerbaijani words. It works as an Azerbaijani `num2words` style converter for
integers, decimals, negative numbers, and numeric strings that use either `.`
or `,` as the decimal separator.

[![PyPI version](https://img.shields.io/pypi/v/aznum2words.svg)](https://pypi.org/project/aznum2words/)
[![Python versions](https://img.shields.io/pypi/pyversions/aznum2words.svg)](https://pypi.org/project/aznum2words/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Typed](https://img.shields.io/badge/typing-typed-blue.svg)](./aznum2words/py.typed)
[![Language: Azerbaijani](https://img.shields.io/badge/lang-az-brightgreen.svg)](./README.az.md)

## Features

- Convert integers to Azerbaijani text: `123` -> `yüz iyirmi üç`
- Convert decimal numbers with Azerbaijani fraction wording
- Handle negative numbers with `mənfi`
- Accept `int`, `float`, `str`, and `Decimal`
- Support both `.` and `,` decimal separators in strings
- Keep `Decimal` fractional precision for amount-style text
- Zero runtime dependencies
- Typed package marker included for type checkers

## Installation

```bash
pip install aznum2words
```

## Quick Start

```python
from decimal import Decimal

from aznum2words import AzerbaijaniNumberConverter, convert, num2words

converter = AzerbaijaniNumberConverter()

converter.convert(123456789)
# "yüz iyirmi üç milyon dörd yüz əlli altı min yeddi yüz səksən doqquz"

convert("1,25")
# "bir tam yüzdə iyirmi beş"

num2words(Decimal("0.001"))
# "sıfır tam mində bir"
```

## Examples

```python
from aznum2words import convert

convert(0)
# "sıfır"

convert(-42)
# "mənfi qırx iki"

convert("1001")
# "min bir"

convert("2.7021")
# "iki tam on mində yeddi min iyirmi bir"
```

## Use Cases

`aznum2words` is useful for Azerbaijani localization, invoices, receipts,
financial documents, legal documents, reports, form generation, and applications
that need to display numbers as Azerbaijani text.

Common search terms for this package include Azerbaijani number to words,
number-to-words Azerbaijani, Azeri num2words, Azerbaijani number converter,
Python numbers to words, and Azerbaijani amount in words.

## API

The package exposes three public imports:

```python
from aznum2words import AzerbaijaniNumberConverter, convert, num2words
```

`convert(number)` and `num2words(number)` use a shared default converter.
Instantiate `AzerbaijaniNumberConverter` when you prefer an explicit converter
object.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

The package supports Python 3.9+ and has no runtime dependencies.
