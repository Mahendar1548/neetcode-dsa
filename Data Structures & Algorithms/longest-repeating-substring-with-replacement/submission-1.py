class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_wise_count = defaultdict(int)
        ans = 0
        start = 0
        s_len = len(s)
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
            print(s_len ,char_wise_count)
            start_char_count = char_wise_count[start]
            window_len = i - start + 1
            av = k - (window_len - start_char_count)
            pv = window_len + (av if av > 0  else 0)
            hv = min(s_len, pv)
            ans = max(ans, hv)
            print(hv, ans, pv, av)

        return ans
