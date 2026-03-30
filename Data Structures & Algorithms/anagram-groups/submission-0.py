from typing import *
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_wise_answers = defaultdict(list)
        for str_val in strs:
            ans = "".join(sorted(str_val))
            anagram_wise_answers[ans].append(str_val)
        
        return list(anagram_wise_answers.values())
