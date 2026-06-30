# aznum2words

Convert integers and decimal numbers to Azerbaijani words.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Language: Azerbaijani](https://img.shields.io/badge/lang-az-brightgreen.svg)](./README.az.md)

## Installation

```bash
pip install aznum2words
```

## Usage

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

Strings may use `.` or `,` as the decimal separator. `Decimal` inputs keep their
written fractional precision, so `Decimal("1.20")` is read as hundredths.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

The package has no runtime dependencies and supports Python 3.9+.
