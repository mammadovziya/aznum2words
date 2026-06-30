# aznum2words - Python üçün Azərbaycan dilində ədədləri sözə çevirən kitabxana

`aznum2words` tam, kəsr və mənfi ədədləri Azərbaycan dilində sözlə ifadə edən
kiçik Python kitabxanasıdır. Kitabxana Azərbaycan dili üçün `num2words` tipli
number-to-words çevirici kimi işləyir və `.` və ya `,` onluq ayırıcılarından
istifadə edən sətir dəyərlərini dəstəkləyir.

[![PyPI versiyası](https://img.shields.io/pypi/v/aznum2words.svg)](https://pypi.org/project/aznum2words/)
[![Python versiyaları](https://img.shields.io/pypi/pyversions/aznum2words.svg)](https://pypi.org/project/aznum2words/)
[![Lisenziya: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Typed](https://img.shields.io/badge/typing-typed-blue.svg)](./aznum2words/py.typed)
[![Dil: English](https://img.shields.io/badge/lang-en-brightgreen.svg)](./README.md)

## Xüsusiyyətlər

- Tam ədədləri Azərbaycan dilində sözə çevirir: `123` -> `yüz iyirmi üç`
- Kəsr ədədləri Azərbaycan dilində düzgün kəsr ifadəsi ilə oxuyur
- Mənfi ədədlər üçün `mənfi` sözündən istifadə edir
- `int`, `float`, `str` və `Decimal` dəyərlərini qəbul edir
- Sətir dəyərlərində `.` və `,` onluq ayırıcılarını dəstəkləyir
- `Decimal` üçün yazılmış kəsr dəqiqliyini saxlayır
- Əlavə runtime asılılığı yoxdur
- Type checker-lər üçün typed paket marker-i var

## Quraşdırma

```bash
pip install aznum2words
```

## Sürətli istifadə

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

## Nümunələr

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

## İstifadə sahələri

`aznum2words` Azərbaycan dili lokalizasiyası, faktura, qəbz, maliyyə sənədləri,
hüquqi sənədlər, hesabatlar, forma generasiyası və ədədləri Azərbaycan dilində
söz kimi göstərən tətbiqlər üçün uyğundur.

Axtarış üçün uyğun ifadələr: Azərbaycan dilində ədədlərin sözlə yazılışı,
Azərbaycan dili number-to-words, Azeri num2words, Python ədədi sözə çevirmə,
Azərbaycan dilində məbləğin yazı ilə göstərilməsi.

## API

Paket üç əsas import təqdim edir:

```python
from aznum2words import AzerbaijaniNumberConverter, convert, num2words
```

`convert(number)` və `num2words(number)` hazır converter obyektindən istifadə
edir. Daha açıq istifadə üçün `AzerbaijaniNumberConverter` ayrıca yaradıla
bilər.

## İnkişaf

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

Kitabxana Python 3.9+ dəstəkləyir və runtime asılılığı yoxdur.
