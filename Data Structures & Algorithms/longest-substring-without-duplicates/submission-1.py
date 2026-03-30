class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        max_window = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in curr_set:
                while s[start] != s[i]:
                    curr_set.remove(s[start])
                    start += 1
                start += 1
            else:
                curr_set.add(s[i])
            max_window = max(max_window, i - start + 1)
        
        return max_window
