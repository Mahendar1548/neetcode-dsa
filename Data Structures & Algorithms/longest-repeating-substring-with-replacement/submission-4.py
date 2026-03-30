class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        l = r = 0
        count = dict()
        ans = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, (r-l+1))
            r += 1
        
        return r - l
