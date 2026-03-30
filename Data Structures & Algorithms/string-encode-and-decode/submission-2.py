from typing import *
from collections import Counter, defaultdict


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str_val in strs:
            str_len = str(len(str_val))
            encoded_str += str(len(str_len)) + str_len + str_val

        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i < len(s):
            str_len_len = int(s[i])
            str_len = int(s[i+1: i+1+ str_len_len])
            ans.append(s[i+1+str_len_len: int(s[i])+i+1+str_len])
            i += 1+str_len_len + str_len
        return ans
