class Solution:
    def numDecodings(self, s: str) -> int:
        last, last_to_last = 1, 0
        str_len = len(s)
        for i in range(str_len):
            curr = 0
            if i > 0 and s[i-1] != '0':
                if int(s[i-1:i+1]) <= 26:
                    curr += last_to_last
            if s[i] != '0':
                curr += last

            last_to_last = last
            last = curr

        return last