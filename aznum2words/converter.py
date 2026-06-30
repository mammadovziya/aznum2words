from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Union

NumberLike = Union[int, float, str, Decimal]


class AzerbaijaniNumberConverter:
    """Convert integers and decimal numbers to Azerbaijani words."""

    ZERO = "sıfır"
    NEGATIVE_WORD = "mənfi"
    POINT_WORD = "tam"
    HUNDRED = "yüz"

    UNITS = (
        "",
        "bir",
        "iki",
        "üç",
        "dörd",
        "beş",
        "altı",
        "yeddi",
        "səkkiz",
        "doqquz",
    )
    TENS = (
        "",
        "on",
        "iyirmi",
        "otuz",
        "qırx",
        "əlli",
        "altmış",
        "yetmiş",
        "səksən",
        "doxsan",
    )
    SCALES = (
        "",
        "min",
        "milyon",
        "milyard",
        "trilyon",
        "kvadrilyon",
        "kvintilyon",
        "sekstilyon",
        "septilyon",
        "oktilyon",
        "nonilyon",
        "desilyon",
    )
    HARD_VOWELS = frozenset("aıou")
    ALL_VOWELS = frozenset("aıoueəiöü")

    def convert(self, number: NumberLike) -> str:
        """Return the Azerbaijani words for *number*.

        Strings may use either "." or "," as the decimal separator.
        Decimal inputs keep their written fractional precision.
        """

        decimal_number = self._to_decimal(number)
        if decimal_number.is_zero():
            return self.ZERO

        sign, integer_part, fraction_digits = self._split_decimal(decimal_number)
        result = self.convert_integer(integer_part)

        if fraction_digits and int(fraction_digits) != 0:
            denominator = self._fraction_denominator(len(fraction_digits))
            fraction_words = self.convert_integer(int(fraction_digits))
            result = f"{result} {self.POINT_WORD} {denominator} {fraction_words}"

        if sign < 0:
            return f"{self.NEGATIVE_WORD} {result}"
        return result

    def convert_integer(self, number: int) -> str:
        """Return the Azerbaijani words for an integer."""

        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("number must be an integer")

        if number < 0:
            return f"{self.NEGATIVE_WORD} {self.convert_integer(-number)}"
        if number == 0:
            return self.ZERO

        parts: list[str] = []
        group = 0

        while number:
            chunk = number % 1000
            if chunk:
                if group >= len(self.SCALES):
                    raise ValueError("number is too large to convert")
                parts.append(self._format_group(chunk, group))

            number //= 1000
            group += 1

        return " ".join(reversed(parts))

    def convert_three_digits(self, number: int) -> str:
        """Return words for a number from 0 to 999."""

        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("number must be an integer")
        if not 0 <= number <= 999:
            raise ValueError("number must be between 0 and 999")
        if number == 0:
            return self.ZERO

        hundred = number // 100
        ten = (number % 100) // 10
        unit = number % 10

        parts: list[str] = []
        if hundred == 1:
            parts.append(self.HUNDRED)
        elif hundred > 1:
            parts.append(f"{self.UNITS[hundred]} {self.HUNDRED}")

        if ten:
            parts.append(self.TENS[ten])
        if unit:
            parts.append(self.UNITS[unit])

        return " ".join(parts)

    def _format_group(self, chunk: int, group: int) -> str:
        chunk_words = self.convert_three_digits(chunk)
        scale = self.SCALES[group]

        if not scale:
            return chunk_words
        if group == 1 and chunk == 1:
            return scale
        return f"{chunk_words} {scale}"

    def _fraction_denominator(self, precision: int) -> str:
        denominator = self.convert_integer(10**precision)
        if precision >= 6 and precision % 3 == 0:
            denominator = denominator.removeprefix("bir ")
        return self._add_locative_suffix(denominator)

    def _add_locative_suffix(self, words: str) -> str:
        prefix, separator, last_word = words.rpartition(" ")
        suffix = "da" if self._last_vowel(last_word) in self.HARD_VOWELS else "də"
        locative_word = f"{last_word}{suffix}"

        if separator:
            return f"{prefix} {locative_word}"
        return locative_word

    def _last_vowel(self, word: str) -> str:
        for letter in reversed(word):
            if letter in self.ALL_VOWELS:
                return letter
        return "ə"

    def _to_decimal(self, number: NumberLike) -> Decimal:
        if isinstance(number, bool):
            raise TypeError("booleans are not supported")

        if isinstance(number, Decimal):
            decimal_number = number
        elif isinstance(number, (int, float)):
            decimal_number = Decimal(str(number))
        elif isinstance(number, str):
            normalized = number.strip().replace(" ", "")
            if not normalized:
                raise ValueError("number cannot be empty")
            if "," in normalized and "." not in normalized:
                normalized = normalized.replace(",", ".")
            try:
                decimal_number = Decimal(normalized)
            except InvalidOperation as exc:
                raise ValueError(f"invalid number: {number!r}") from exc
        else:
            raise TypeError("number must be an int, float, str, or Decimal")

        if not decimal_number.is_finite():
            raise ValueError("number must be finite")
        return decimal_number

    def _split_decimal(self, number: Decimal) -> tuple[int, int, str]:
        sign = -1 if number < 0 else 1
        decimal_tuple = abs(number).as_tuple()
        digits = "".join(str(digit) for digit in decimal_tuple.digits)
        exponent = decimal_tuple.exponent

        if exponent >= 0:
            return sign, int(digits + ("0" * exponent)), ""

        precision = -exponent
        padded_digits = digits.zfill(precision + 1)
        split_at = len(padded_digits) - precision
        integer_digits = padded_digits[:split_at] or "0"
        fraction_digits = padded_digits[split_at:]

        return sign, int(integer_digits), fraction_digits


_DEFAULT_CONVERTER = AzerbaijaniNumberConverter()


def convert(number: NumberLike) -> str:
    """Return the Azerbaijani words for *number* using the default converter."""

    return _DEFAULT_CONVERTER.convert(number)


num2words = convert
