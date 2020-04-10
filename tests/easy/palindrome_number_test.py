import sys
import unittest

from solutions.easy import palindrome_number


class PalindromeNumberTestCase(unittest.TestCase):
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (-10, False),
        (101, True),
        (10101, True),
        (9223372036854775807, False),       # Max 64-bit int
        (-9223372036854775807 - 1, False),  # Min 64-bit int
        (1, True),
        (-1, False)
    ]

    def test(self):
        for test_case in self.test_cases:
            self.assertEqual(palindrome_number.is_palindrome(test_case[0]), test_case[1])


if __name__ == '__main__':
    unittest.main()
