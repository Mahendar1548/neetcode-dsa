from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:len(s1)-1])
        start = 0
        for i in range(len(s1)-1, len(s2)):
            window_counter[s2[i]] = 1 + window_counter.get(s2[i], 0)
            for key in s1_counter:
                if s1_counter[key] != window_counter.get(key, 0):
                    break
            else:
                return True
            window_counter[s2[start]] -= 1
            start += 1

        return False
