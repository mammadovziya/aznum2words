# aznum2words

Tam və kəsr ədədləri Azərbaycan dilində sözlə ifadə edən kiçik Python
kitabxanası.

[![Lisenziya: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Dil: English](https://img.shields.io/badge/lang-en-brightgreen.svg)](./README.md)

## Quraşdırma

```bash
pip install aznum2words
```

## İstifadə

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

Sətir kimi verilən ədədlərdə onluq ayırıcı üçün `.` və ya `,` istifadə etmək
olar. `Decimal` dəyərlərində yazılmış kəsr dəqiqliyi saxlanılır; məsələn,
`Decimal("1.20")` yüzdəlik kimi oxunur.

## İnkişaf

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

Kitabxananın işləməsi üçün əlavə asılılıq yoxdur və Python 3.9+ dəstəklənir.
