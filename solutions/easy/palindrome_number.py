def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    s1 = str(x)
    s2 = s1[::-1]

    return s1 == s2
