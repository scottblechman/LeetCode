from solutions.easy.roman_to_integer import  roman_to_integer


def test_roman_to_integer():
    assert roman_to_integer("III") == 3
    assert roman_to_integer("IV") == 4
    assert roman_to_integer("IX") == 9
    assert roman_to_integer("LVIII") == 58
    assert roman_to_integer("MCMXCIV") == 1994
