from decimal import Decimal

import pytest

from aznum2words import AzerbaijaniNumberConverter, convert, num2words


@pytest.fixture
def converter():
    return AzerbaijaniNumberConverter()


@pytest.mark.parametrize(
    ("number", "words"),
    [
        (0, "sıfır"),
        (5, "beş"),
        (10, "on"),
        (19, "on doqquz"),
        (42, "qırx iki"),
        (100, "yüz"),
        (101, "yüz bir"),
        (1000, "min"),
        (1001, "min bir"),
        (2000, "iki min"),
        (1_000_000, "bir milyon"),
        (
            123_456_789,
            "yüz iyirmi üç milyon dörd yüz əlli altı min yeddi yüz səksən doqquz",
        ),
        (
            12_345_678_901_234_567,
            "on iki kvadrilyon üç yüz qırx beş trilyon altı yüz yetmiş səkkiz "
            "milyard doqquz yüz bir milyon iki yüz otuz dörd min beş yüz altmış yeddi",
        ),
    ],
)
def test_convert_integers(converter, number, words):
    assert converter.convert(number) == words


def test_convert_negative_number(converter):
    assert converter.convert(-123) == "mənfi yüz iyirmi üç"


@pytest.mark.parametrize(
    ("number", "words"),
    [
        (123.4567, "yüz iyirmi üç tam on mində dörd min beş yüz altmış yeddi"),
        ("1,25", "bir tam yüzdə iyirmi beş"),
        ("1.05", "bir tam yüzdə beş"),
        (Decimal("0.001"), "sıfır tam mində bir"),
        (Decimal("0.000001"), "sıfır tam milyonda bir"),
        (-2.7021, "mənfi iki tam on mində yeddi min iyirmi bir"),
    ],
)
def test_convert_fractional_numbers(converter, number, words):
    assert converter.convert(number) == words


def test_convenience_functions():
    assert convert(7) == "yeddi"
    assert num2words(80) == "səksən"


@pytest.mark.parametrize("number", [True, float("nan"), "not-a-number"])
def test_invalid_numbers_raise(converter, number):
    with pytest.raises((TypeError, ValueError)):
        converter.convert(number)
