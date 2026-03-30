from typing import *
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        s_char_wise_count = Counter(s)
        t_char_wise_count = Counter(t)
        for char in s_char_wise_count:
            if s_char_wise_count[char] != t_char_wise_count[char]:
                return False
        return True
