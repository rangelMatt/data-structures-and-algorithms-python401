import pytest
from code_challenges.roman_numerals import roman_to_arabic

def test_rome_num():
    roman = 'VI'
    actual = roman_to_arabic(roman)
    expected = 6
    assert actual == expected

def test_rome_num1():
    roman = 'XLVIII'
    actual = roman_to_arabic(roman)
    expected = 48
    assert actual == expected

def test_rome_num2():
    roman = 'MCMLXXXIV'
    actual = roman_to_arabic(roman)
    expected = 1984
    assert actual == expected

def test_rome_num3():
    roman = 'MC'
    actual = roman_to_arabic(roman)
    expected = 1100
    assert actual == expected

def test_rome_num4():
    roman = 'CM'
    actual = roman_to_arabic(roman)
    expected = 900
    assert actual == expected

def test_rome_num5():
    roman = 'CMI'
    actual = roman_to_arabic(roman)
    expected = 901
    assert actual == expected

def test_rome_num6():
    roman = 'CMIX'
    actual = roman_to_arabic(roman)
    expected = 909
    assert actual == expected

def test_rome_num7():
    roman = 'CMXVI'
    actual = roman_to_arabic(roman)
    expected = 916
    assert actual == expected
