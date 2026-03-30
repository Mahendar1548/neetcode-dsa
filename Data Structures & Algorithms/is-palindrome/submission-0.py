import string
from typing import *
from collections import Counter, defaultdict


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            left_char = s[left_pointer]
            right_char = s[right_pointer]
            if "A" <= left_char <= "Z":
                left_char = left_char.lower()
            if "A" <= right_char <= "Z":
                right_char = right_char.lower()

            if left_char not in string.ascii_letters + string.digits:
                left_pointer += 1
                continue
            if right_char not in string.ascii_letters + string.digits:
                right_pointer -= 1
                continue

            if left_char != right_char:
                return False

            left_pointer += 1
            right_pointer -= 1

        return True

