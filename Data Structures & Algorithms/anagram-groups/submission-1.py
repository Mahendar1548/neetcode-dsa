from typing import *
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_wise_answers = defaultdict(list)
        for str_val in strs:
            char_map = [0]*26
            for char in str_val:
                char_map[ord(char)-ord('a')] += 1

            anagram_wise_answers[tuple(char_map)].append(str_val)

        return list(anagram_wise_answers.values())
