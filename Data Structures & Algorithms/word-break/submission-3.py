class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * len(s)

        def dfs(idx):
            print(idx)
            if idx >= len(s):
                return True
            if dp[idx] is not None:
                return dp[idx]

            is_breakable = False
            for word in wordDict:
                word_len = len(word)
                if not is_breakable and word == s[idx:idx+word_len]:
                    # print(word)
                    is_breakable = dfs(idx+word_len)
            dp[idx] = is_breakable
            return is_breakable
        
        return dfs(0)