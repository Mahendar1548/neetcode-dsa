class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_wise_count = defaultdict(int)
        ans = 0
        start = 0
        for i, char in enumerate(s):
            char_wise_count[char] += 1
            while start < i:
                start_char_count = char_wise_count[s[start]]
                window_len = i - start + 1
                if start_char_count + k >= window_len:
                    break
                else:
                    char_wise_count[s[start]] -= 1
                    start += 1

            window_len = i - start + 1
            ans = max(ans, window_len)
        
        return ans
