from solutions.easy.palindrome_number import is_palindrome


def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
    assert is_palindrome(-101) is False
